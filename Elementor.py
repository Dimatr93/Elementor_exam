
import json
import requests

class VirusTotal:

    def __init__(self):
        self.url_scan = 'https://www.virustotal.com/vtapi/v2/file/scan'
        self.url_download= 'https://www.virustotal.com/vtapi/v2/file/download'
        self.url_report = 'https://www.virustotal.com/vtapi/v2/file/report'
        self.file='./request1.csv'
        #self.file='https://elementor-pub.s3.eu-central-1.amazonaws.com/Data-Enginner/Challenge1/request1.csv'
        self.apikey='9d3f6864bff452134776222a0ceb13fcf722e375449164b22fabedfd04f95302'
        self.sha256=[]


    def scan(self):

       url = self.url_scan
       params = {'apikey':self.apikey}
       files = {'file': (self.file, open(self.file, 'rb'))}
       response = requests.post(url, files=files, params=params)
       response_text=json.loads(response.text)
       print(response.json())
       self.sha256 = response_text['sha256']
       print(self.sha256)

    def download(self):

       url = self.url_download
       params = {'apikey':self.apikey, 'hash': self.sha256}
       response = requests.get(url, params=params)
       print(response.content)



    def report(self):

       url =self.url_report

       params = {'apikey':self.apikey, 'resource':self.sha256}

       response = requests.get(url, params=params)

       print(response.json())






MS= VirusTotal()
MS.scan()
MS.download()
MS.report()
