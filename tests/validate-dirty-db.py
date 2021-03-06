#!/usr/bin/env python3

from testUtils import Utils
from Cluster import Cluster
from TestHelper import TestHelper

import random
import subprocess
import signal

###############################################################
# Test for validating the dirty db flag sticks repeated myeosnode restart attempts
###############################################################


Print=Utils.Print

def errorExit(msg="", errorCode=1):
    Print("ERROR:", msg)
    exit(errorCode)

args = TestHelper.parse_args({"--keep-logs","--dump-error-details","-v","--leave-running","--clean-run"})
debug=args.v
pnodes=1
topo="mesh"
delay=1
chainSyncStrategyStr=Utils.SyncResyncTag
total_nodes = pnodes
killCount=1
killSignal=Utils.SigKillTag

killEnuInstances= not args.leave_running
dumpErrorDetails=args.dump_error_details
keepLogs=args.keep_logs
killAll=args.clean_run

seed=1
Utils.Debug=debug
testSuccessful=False

def runEnunodeAndGetOutput(myNodeId, myTimeout=3):
    """Startup myeosnode, wait for timeout (before forced shutdown) and collect output. Stdout, stderr and return code are returned in a dictionary."""
    Print("Launching myeosnode process id: %d" % (myNodeId))
    cmd="programs/myeosnode/myeosnode --config-dir etc/myeosio/node_bios --data-dir var/lib/node_bios --verbose-http-errors"
    Print("cmd: %s" % (cmd))
    proc=subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output={}
    try:
        outs,errs = proc.communicate(timeout=myTimeout)
        output["stdout"] = outs.decode("utf-8")
        output["stderr"] = errs.decode("utf-8")
        output["returncode"] = proc.returncode
    except (subprocess.TimeoutExpired) as _:
        Print("ERROR: Enunode is running beyond the defined wait time. Hard killing myeosnode instance.")
        proc.send_signal(signal.SIGKILL)
        return (False, None)

    return (True, output)

random.seed(seed) # Use a fixed seed for repeatability.
cluster=Cluster(mykeosdd=True)

try:
    cluster.setChainStrategy(chainSyncStrategyStr)

    cluster.killall(allInstances=killAll)
    cluster.cleanup()

    Print ("producing nodes: %d, topology: %s, delay between nodes launch(seconds): %d, chain sync strategy: %s" % (
        pnodes, topo, delay, chainSyncStrategyStr))

    Print("Stand up cluster")
    if cluster.launch(pnodes, total_nodes, topo=topo, delay=delay, dontBootstrap=True) is False:
        errorExit("Failed to stand up myeos cluster.")

    node=cluster.getNode(0)
    if node is None:
        errorExit("Cluster in bad state, received None node")

    Print("Kill cluster nodes.")
    cluster.killall(allInstances=killAll)
    
    Print("Restart myeosnode repeatedly to ensure dirty database flag sticks.")
    nodeId=0
    timeout=3
    
    for i in range(0,3):
        Print("Attempt %d." % (i))
        ret = runEnunodeAndGetOutput(nodeId, timeout)
        assert(ret)
        assert(isinstance(ret, tuple))
        if not ret or not ret[0]:
            exit(1)

        assert(ret[1])
        assert(isinstance(ret[1], dict))
        # pylint: disable=unsubscriptable-object
        stderr= ret[1]["stderr"]
        retCode=ret[1]["returncode"]
        assert(retCode == 2)
        assert("database dirty flag set" in stderr)

    testSuccessful=True
finally:
    TestHelper.shutdown(cluster, None, testSuccessful, killEnuInstances, False, keepLogs, killAll, dumpErrorDetails)

exit(0)
