#pragma once

#include <eosiolib/eosio.hpp>
#include <eosiolib/transaction.hpp>

namespace eosio {

   class sudo : public contract {
      public:
         sudo( account_name self ):contract(self){}

         void propose();
         void approve( account_name proposer, name proposal_name, account_name approver );
         void unapprove( account_name proposer, name proposal_name, account_name unapprover );
         void cancel( account_name proposer, name proposal_name, account_name canceler );
         void exec( account_name proposer, name proposal_name, account_name executer );

      private:
         struct proposal {
            name                    proposal_name;
            vector<char>            packed_transaction;

            auto primary_key()const { return proposal_name.value; }
         };
         typedef eosio::multi_index<N(proposal),proposal> proposals;

         struct approvals_info {
            name                                      proposal_name;
            boost::container::flat_set<account_name>  provided_approvals;

            auto primary_key()const { return proposal_name.value; }
         };
         typedef eosio::multi_index<N(approvals),approvals_info> approvals;
   };

} /// namespace eosio