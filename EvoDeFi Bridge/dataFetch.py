# Import libraries
import requests
import csv

# Etherscan API Setup
URL = "https://api.bscscan.com"
API_KEY = "W9KUR7P8P2HU1R589IS48X4WVJV5B6Z8XC"
START_BLOCK = "7929701" # ~ 2nd June 2021 04:38 AM IST
END_BLOCK = "7939660" # ~ 2nd June 2021 12:57 PM IST
CONTRACT_ADDRESS = "0x3247554B2baD31D5120b98d5F51Df5A406d6B524"

endpoint = "{}/api?module=account&action=tokentx&address={}&startblock={}&endblock={}&offset=10&sort=asc&apikey={}".format(URL ,CONTRACT_ADDRESS, START_BLOCK, END_BLOCK, API_KEY)

# Calling API and saving data as json
response = requests.get(endpoint)
JSON_DATA_RAW = response.json()
JSON_DATA = JSON_DATA_RAW['result']

# Converting JSON data to CSV
EVODEFIBRDIGE = open('./evodefi.csv', 'w')
csv_writer = csv.writer(EVODEFIBRDIGE)

count = 0
for transaction in JSON_DATA:
    if count == 0:
        header = transaction.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(transaction.values())