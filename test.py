import pivx_quark_hash as quark_hash
from binascii import unhexlify, hexlify

import unittest

# PIVX Genesis Block
# {
#     "hash" : "0000041e482b9b9691d98eefb48473405c0b8ec31b76df3797c74a78680ef818",
#     "confirmations" : 1002162,
#     "size" : 302,
#     "height" : 0,
#     "version" : 1,
#     "merkleroot" : "1b2ef6e2f28be914103a277377ae7729dcd125dfeb8bf97bd5964ba72b6dc39b",
#     "acc_checkpoint" : "0000000000000000000000000000000000000000000000000000000000000000",
#     "tx" : [
#         "1b2ef6e2f28be914103a277377ae7729dcd125dfeb8bf97bd5964ba72b6dc39b"
#     ],
#     "time" : 1454124731,
#     "nonce" : 2402015,
#     "bits" : "1e0ffff0",
#     "difficulty" : 0.00024414,
#     "chainwork" : "0000000000000000000000000000000000000000000000000000000000100010",
#     "nextblockhash" : "000005504fa4a6766e854b2a2c3f21cd276fd7305b84f416241fd4431acbd12d",
#     "moneysupply" : 0.00000000,
#     "zPIVsupply" : {
#         "1" : 0.00000000,
#         "5" : 0.00000000,
#         "10" : 0.00000000,
#         "50" : 0.00000000,
#         "100" : 0.00000000,
#         "500" : 0.00000000,
#         "1000" : 0.00000000,
#         "5000" : 0.00000000,
#         "total" : 0.00000000
#     }
# }
#
# # PIVX Block n. 100
# {
#     "hash" : "0000000a86f23294329c83d69e254a4f8d127b6b899a14b147885740c4be1713",
#     "confirmations" : 1002076,
#     "size" : 196,
#     "height" : 100,
#     "version" : 3,
#     "merkleroot" : "ff1e9afc003aae570d0991aca5c79c17949f04999b14bded8510c3d410fffaf2",
#     "acc_checkpoint" : "0000000000000000000000000000000000000000000000000000000000000000",
#     "tx" : [
#         "ff1e9afc003aae570d0991aca5c79c17949f04999b14bded8510c3d410fffaf2"
#     ],
#     "time" : 1454186818,
#     "nonce" : 19412647,
#     "bits" : "1d0b17c1",
#     "difficulty" : 0.09014728,
#     "chainwork" : "0000000000000000000000000000000000000000000000000000000130173d27",
#     "previousblockhash" : "00000008620a75a488dd346a668da5862a724479d66d35618b938912d59d0062",
#     "nextblockhash" : "00000002a284169ee5b3be7a5622ed18bc18f8b8f73c713a7589d7c4813fa05c",
#     "moneysupply" : 84751.00000000,
#     "zPIVsupply" : {
#         "1" : 0.00000000,
#         "5" : 0.00000000,
#         "10" : 0.00000000,
#         "50" : 0.00000000,
#         "100" : 0.00000000,
#         "500" : 0.00000000,
#         "1000" : 0.00000000,
#         "5000" : 0.00000000,
#         "total" : 0.00000000
#    }
# }

header_hex = "0100000000000000000000000000000000000000000000000000000000000000000000009bc36d2ba74b96d57bf98bebdf25d1dc2977ae7773273a1014e98bf2e2f62e1bbb2eac56f0ff0f1edfa624000101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff5e04ffff001d01044c55552e532e204e657773202620576f726c64205265706f7274204a616e203238203230313620576974682048697320416273656e63652c205472756d7020446f6d696e6174657320416e6f7468657220446562617465ffffffff0100ba1dd205000000434104c10e83b2703ccf322f7dbd62dd5855ac7c10bd055814ce121ba32607d573b8810c02c0582aed05b4deb9c4b77b26d92428c61256cd42774babea0a073b2ed0c9ac00000000"
best_hash = '0000041e482b9b9691d98eefb48473405c0b8ec31b76df3797c74a78680ef818'

header_hex2 = "0300000062009dd51289938b61356dd67944722a86a58d666a34dd88a4750a6208000000f2faff10d4c31085edbd149b99049f94179cc7a5ac91090d57ae3a00fc9a1eff4221ad56c1170b1da73628010101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1e0164044221ad56085ffffffe420000000d2f6e6f64655374726174756d2f000000000100ba1dd2050000001976a91424609e364dc7ce4f118b49e03d2106cc435dae3088ac00000000"
best_hash2 = '0000000a86f23294329c83d69e254a4f8d127b6b899a14b147885740c4be1713'
 
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash
        self.block_header2 = unhexlify(header_hex2)
        self.best_hash2 = best_hash2

    def test_quark_hash(self):
        self.pow_hash = hexlify(quark_hash.getPoWHash(self.block_header)[::-1]).decode('utf-8')
        self.assertEqual(self.pow_hash, self.best_hash)
        
    def test_quark_hash2(self):
        self.pow_hash2 = hexlify(quark_hash.getPoWHash(self.block_header2)[::-1]).decode('utf-8')
        self.assertEqual(self.pow_hash2, self.best_hash2)


if __name__ == '__main__':
    unittest.main()
