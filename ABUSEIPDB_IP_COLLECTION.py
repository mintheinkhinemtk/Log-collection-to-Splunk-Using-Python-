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
    'Key': 'ac542df0b376dfd3af483f258e482526bdd200cb0dcfc4d972dc5dbd664a6f4a730128d0b2cedc51'
}

response = requests.request(method='GET', url=url, headers=headers, params=parameters)

#converting json string type to associated dict data type
decodedResponse = json.loads(response.text)

df = pd.DataFrame(decodedResponse["data"]) # change dict type to dataframe in pandas

df.to_csv('ABUSEIPDB_IPs.csv',index=False) # Changing to csv file, index=False for excluding unnecessary column