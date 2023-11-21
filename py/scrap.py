from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='This helps to pass variables using the cli')
parser.add_argument('--buildurl', action='store', type=str, help='Enters the build url')
args = parser.parse_args()
buildurl=args.buildurl


url=f"{buildurl}/console"

username = 'pocket'
password = 'pocket'

response=requests.get(url, auth=(username, password)).text
soup=BeautifulSoup(url,'lxml')
console=soup.find('pre',class_='console-output').text
print(console)
