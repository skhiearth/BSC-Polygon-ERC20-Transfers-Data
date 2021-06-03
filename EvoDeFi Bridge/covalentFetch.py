# Import libraries
import requests
import csv

# Add column names to CSV file
with open('Data/evoDeFiPolygon.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["TxHash", "Block_Time", "Block_Height", "Gas", "User_Address", "From", "To", "Token_Contract", "Value"])
    
# Etherscan API Setup
URL = "https://api.covalenthq.com/v1"
ID = "137"
CONTRACT_ADDRESS = "0xBCA17c85F7E965ae6f5D05769D300e59221CF1e2"
PAGE_SIZE = "100000"
API_KEY="ckey_10446544a51944ffa7c6603a9e4"
PRIMER = "{\"$match\":{\"decoded.name\":\"Transfer\"}}"

endpoint = "{}/{}/address/{}/transactions_v2/?&page-size={}&key={}?q={}".format(URL, ID, CONTRACT_ADDRESS, PAGE_SIZE, API_KEY, PRIMER)

# Calling API and saving data as json
response = requests.get(endpoint)
JSON_DATA_RAW = response.json()
JSON_DATA = JSON_DATA_RAW['data']['items']

# Iterate over JSON
for txn in JSON_DATA:
    LIST_TO_ADD = []
    if(txn["successful"]):
        TX_HASH = txn["tx_hash"]
        LIST_TO_ADD.append(txn["tx_hash"])
        if(len(txn["log_events"]) >= 3):
            BLOCKTIME = txn["log_events"][2]["block_signed_at"]
            LIST_TO_ADD.append(txn["log_events"][2]["block_signed_at"])
            BLOCKHEIGHT = txn["log_events"][2]["block_height"]
            LIST_TO_ADD.append(txn["log_events"][2]["block_height"])
            GAS = txn["gas_spent"]
            LIST_TO_ADD.append(txn["gas_spent"])
            USERS_ADDRESS = txn["from_address"]
            LIST_TO_ADD.append(txn["from_address"])
            if(txn["log_events"][2]["decoded"]):
                if(txn["log_events"][2]["decoded"]["name"]):
                    if(txn["log_events"][2]["decoded"]["name"] == "Transfer"):
                        FROM = txn["log_events"][2]["decoded"]["params"][0]["value"]
                        LIST_TO_ADD.append(txn["log_events"][2]["decoded"]["params"][0]["value"])
                        TO = txn["log_events"][2]["decoded"]["params"][1]["value"]
                        LIST_TO_ADD.append(txn["log_events"][2]["decoded"]["params"][1]["value"])
                        TOKENCONTRACT = txn["log_events"][2]["sender_address"]
                        LIST_TO_ADD.append(txn["log_events"][2]["sender_address"])
                        VALUE = txn["log_events"][2]["decoded"]["params"][2]["value"]
                        LIST_TO_ADD.append(txn["log_events"][2]["decoded"]["params"][2]["value"])

                        with open('Data/evoDeFiPolygon.csv', 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(LIST_TO_ADD)
                            file.close()
                    else:
                        continue
        else:
            continue
            

# # Converting JSON data to CSV
# EVODEFIBRDIGE = open('./evodefi.csv', 'w')
# csv_writer = csv.writer(EVODEFIBRDIGE)

# count = 0
# for transaction in JSON_DATA:
#     if count == 0:
#         header = transaction.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(transaction.values())