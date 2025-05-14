# Threat Intelligence Automation with VirusTotal & Splunk
#Getting json api response from virustotal with the IP Addresses coming out of Abuseipdb API and gathering those json #response logs to Splunk using a script with Python 


#Firstly, get an IP list with confidence level at least 75% or 90% from abuseipdb using your abuseipdb api key by running #the script ABUSEIPDB_IP_COLLECTION.py

#The given csv file is the sample list I got from using its api key

#ABUSEIPDB only gives free api requests limited for 5 times at most, that's why, you need to save them in a csv file unless you have paid api key

#From this step, run main.py for inputting IP Input with the ones from your csv to virustotal api and send the necessary response as json to local your splunk server using its HEC token

# You need to generate HEC token from your local splunk server as the data is collected using http protocol
