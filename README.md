# MyEOSIO - The Most Powerful Infrastructure for Decentralized Applications

Welcome to the MyEOSIO source code repository! This software enables businesses to rapidly build and deploy high-performance and high-security blockchain-based applications.

Some of the groundbreaking features of MyEOSIO include:

1. Free Rate Limited Transactions 
1. Low Latency Block confirmation (0.5 seconds)
1. Low-overhead Byzantine Fault Tolerant Finality
1. Designed for optional high-overhead, low-latency BFT finality 
1. Smart contract platform powered by Web Assembly
1. Designed for Sparse Header Light Client Validation
1. Scheduled Recurring Transactions 
1. Time Delay Security
1. Hierarchical Role Based Permissions
1. Support for Biometric Hardware Secured Keys (e.g. Apple Secure Enclave)
1. Designed for Parallel Execution of Context Free Validation Logic
1. Designed for Inter Blockchain Communication 

MyEOSIO is released under the open source MIT license and is offered “AS IS” without warranty of any kind, express or implied. Any security provided by the MyEOSIO software depends in part on how it is used, configured, and deployed. MyEOSIO is built upon many third-party libraries such as Binaryen (Apache License)and WAVM  (BSD 3-clause) which are also provided “AS IS” without warranty of any kind. Without limiting the generality of the foregoing, Block.one makes no representation or guarantee that MyEOSIO or any third-party libraries will perform as intended or will be free of errors, bugs or faulty code. Both may fail in large or small ways that could completely or partially limit functionality or compromise computer systems. If you use or implement MyEOSIO, you do so at your own risk. In no event will Block.one be liable to any party for any damages whatsoever, even if it had been advised of the possibility of damage.  

ERL.one is neither launching nor operating any initial public blockchains based upon the MyEOSIO software. This release refers only to version 1.0 of our open source software. We caution those who wish to use blockchains built on MyEOSIO to carefully vet the companies and organizations launching blockchains based on MyEOSIO before disclosing any private keys to their derivative software. 

There is no public testnet running currently.

## Supported Operating Systems
MyEOSIO currently supports the following operating systems:  
1. Amazon 2017.09 and higher
2. Centos 7
3. Fedora 25 and higher (Fedora 27 recommended)
4. Mint 18
5. Ubuntu 16.04 (Ubuntu 16.10 recommended)
6. Ubuntu 18.04
7. MacOS Darwin 10.12 and higher (MacOS 10.13.x recommended)

# Resources
1. [MyEOSIO Website](https://myeosio.org)
2. [MyEOSIO Forum](https://myeosio.com)
3. [Community Telegram Group](https://t.me/myeosiochat)

# Running
To download MyEOSIO, the git clone command is:
```bash
git clone https://github.com/bithacks-tech/myeosio --recursive
```
Then run the following script for the first time:
```bash
./myeosio_build.sh
```
Remember waiting for the code to be successfully built. Then run the following command to install the environment of MyEOSIO:
```bash
cd build
sudo make install
```
Wait for the accomplishment of the installation.
