import requests
import time
import json
import datetime
from datetime import timezone
import os

IP = []

def sent(ip):
    if not os.path.exists('collected_IPs.txt'):
        return False
    with open('collected_IPs.txt','r') as f:
        if ip in f.read().splitlines():
            return True


with open('ABUSEIPDB_IPs.csv','r') as IP_f:
    lines = IP_f.readlines()
    for i in range(1,len(lines)):
        data_list = lines[i].split(',')
        IP.append(data_list[0]) # appending IP Address

#splunk_server
splunk_url = 'http://127.0.0.1:8088/services/collector/event'
HEC_token = 'your-Splunk-HEC-token'

splunk_headers = {'Authorization':f'Splunk {HEC_token}',
                  'Content-Type':'application/json'}



#virustotal
headers = {
        "accept": "application/json",
        "x-apikey": "your-virustotal-api-key"
    }
import_results = [] # data imported from api response of virustotal
for i in range(len(IP)):
    if sent(IP[i]):
        print(f"Skipping {IP[i]}. This has been already sent.")
        continue
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{IP[i]}"
    response = requests.get(url, headers=headers)
    print(f"VirusTotal response code = {response}")
    if response.status_code == 200:
        data = response.json()
        reputation = data["data"]["attributes"]["reputation"]
        IP_address = data["data"]["id"]
        results = data["data"]["attributes"]["last_analysis_results"].values()
        
        malicious_score = sum(1 for category in results if category['category']=="malicious" ) # getting total scores of 'malicious' category
        print(malicious_score)

        import_results = [result for result in results if result['category'] == "malicious"]

        analyzed_data = []
        for res in import_results:
            data = {
            'Engine':res['engine_name'],
            'Method':res['method'],
            'Result':res['result']
            }
            analyzed_data.append(data)
        
        event_data ={
            "index":"main",
            "sourcetype":"virustotal",
            "event":{
                "IP":IP_address,
                "score":malicious_score,
                "Data":analyzed_data
            }
        }
        HEC_response = requests.post(splunk_url,
                                     headers=splunk_headers,
                                     data = json.dumps(event_data),verify=False)
        print(f"HEC response = {HEC_response.status_code}")
        with open('collected_IPs.txt','a') as md:
            md.write(f'{IP[i]}\n')
        time.sleep(20)
    else:
        print(f'Dats is not collected.\nstatus code is {response.status_code}, and IP Address = {IP[i]}')



