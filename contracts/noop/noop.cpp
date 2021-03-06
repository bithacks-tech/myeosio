/**
 *  @file
 *  @copyright defined in myeosio/LICENSE.txt
 */

#include <myeoslib/myeos.hpp>

namespace myeosio {

   class noop: public contract {
      public:
         noop( account_name self ): contract( self ) { }
         void anyaction( account_name from,
                         const std::string& /*type*/,
                         const std::string& /*data*/ )
         {
            require_auth( from );
         }
   };

   MYEOSIO_ABI( noop, ( anyaction ) )

} /// myeosio     
