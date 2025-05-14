import requests
import json
import pandas as pd
# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/blacklist'

parameters = {
    'confidenceMinimum':'90'
}

headers = {
    'Accept': 'application/json',
    'Key': 'abuseipdb-key'
}

response = requests.request(method='GET', url=url, headers=headers, params=parameters)

#converting json string type to associated dict data type
decodedResponse = json.loads(response.text)

df = pd.DataFrame(decodedResponse["data"]) # change dict type to dataframe in pandas

df.to_csv('ABUSEIPDB_IPs.csv',index=False) # Changing to csv file, index=False for excluding unnecessary column
