# Import libraries
import requests
import csv
import pandas as pd

# BSCScan API Setup
URL = "https://api.etherscan.io"
API_KEY = "9KDCGM8H25R414U4U5IVP4TEJQ91Y7AZC5"
START_BLOCK = "7906054"
END_BLOCK = "7915038"
CONTRACT_ADDRESS = "W9KUR7P8P2HU1R589IS48X4WVJV5B6Z8XC"

endpoint = "{}/api?module=account&action=tokentx&address={}&startblock={}&endblock={}&offset=10&sort=asc&apikey={}".format(URL ,CONTRACT_ADDRESS, START_BLOCK, END_BLOCK, API_KEY)

df = pd.read_csv('maticbridge.csv')

for index, row in df.iterrows():
    print(row)