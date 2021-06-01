# Import libraries
import requests
import csv

# Etherscan API Setup
URL = "https://api.etherscan.io"
API_KEY = "9KDCGM8H25R414U4U5IVP4TEJQ91Y7AZC5"
START_BLOCK = "12546134" # ~ 1st June 2021 08:47 AM IST
END_BLOCK = "12548142" # ~ 1st June 2021 4:24 PM IST
CONTRACT_ADDRESS = "0x40ec5B33f54e0E8A33A975908C5BA1c14e5BbbDf"

endpoint = "{}/api?module=account&action=tokentx&address={}&startblock={}&endblock={}&offset=10&sort=asc&apikey={}".format(URL ,CONTRACT_ADDRESS, START_BLOCK, END_BLOCK, API_KEY)

# Calling API and saving data as json
response = requests.get(endpoint)
JSON_DATA_RAW = response.json()
JSON_DATA = JSON_DATA_RAW['result']

# Converting JSON data to CSV
MATIC_BRIDGE = open('./maticbridge.csv', 'w')
csv_writer = csv.writer(MATIC_BRIDGE)

count = 0
for transaction in JSON_DATA:
    if count == 0:
        header = transaction.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(transaction.values())