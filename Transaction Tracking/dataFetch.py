# Import libraries
import requests
import csv

# Etherscan API Setup
URL = "https://api.etherscan.io"
API_KEY = "9KDCGM8H25R414U4U5IVP4TEJQ91Y7AZC5"
START_BLOCK = "12540855" # ~ May-31-2021 07:43:05 AM +UTC
END_BLOCK = "12588145" # ~ Jun-07-2021 03:15:58 PM +UTC
CONTRACT_ADDRESS = "0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf"

endpoint = "{}/api?module=account&action=tokentx&address={}&startblock={}&endblock={}&offset=10&sort=asc&apikey={}".format(URL ,CONTRACT_ADDRESS, START_BLOCK, END_BLOCK, API_KEY)

# Calling API and saving data as json
response = requests.get(endpoint)
JSON_DATA_RAW = response.json()
JSON_DATA = JSON_DATA_RAW['result']

# Converting JSON data to CSV
MATIC_BRIDGE = open('./posbridge.csv', 'w')
csv_writer = csv.writer(MATIC_BRIDGE)

count = 0
for transaction in JSON_DATA:
    if count == 0:
        header = transaction.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(transaction.values())