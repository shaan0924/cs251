from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cUpmVKMiKhk9aen1FXC4qN4WZWd1K3NBST6FLhEQoeoSzPwS8tmR')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cTr5FbeYZKmvKdjJ8cTmy48QiwvAJ1o8X1fQK5mpVMmaQSvhvNM4')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cSyxgurKxLgAczvvua2CATgts1YxD2G7QUKwHf5ykBytpnqADDiZ')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
   2, my_public_key, cust1_public_key, cust2_public_key, cust3_public_key, 4, OP_CHECKMULTISIGVERIFY, OP_DUP,
my_public_key, OP_EQUALVERIFY, OP_CHECKSIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00008 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '2dc9e5e8229fac4274d24b6ae063a8cc880d0cc7654bb0867813bb4b68e70166')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
