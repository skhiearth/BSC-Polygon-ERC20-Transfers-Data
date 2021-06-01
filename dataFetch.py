# Import libraries
import json
from web3 import Web3

# # Provider
# w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/237478b13272447fbf8b88b4bd9cd01d'))

# # Opening ABI JSON file
# f = open('abi.json',)
# data = json.load(f)

# contract = w3.eth.contract(address='0x000000000000000000000000000000000000dEaD', abi=data)
# print(contract.all_functions())

URL = "https://api.etherscan.io"
API_KEY = "9KDCGM8H25R414U4U5IVP4TEJQ91Y7AZC5"
START_BLOCK = "12546134"
END_BLOCK = "12548142"
CONTRACT_ADDRESS = "0x40ec5B33f54e0E8A33A975908C5BA1c14e5BbbDf"

endpoint = "{}/api?module=account&action=tokentx&address={}&startblock={}&endblock={}&offset=10&sort=asc&apikey={}".format(URL ,CONTRACT_ADDRESS, START_BLOCK, END_BLOCK, API_KEY)

