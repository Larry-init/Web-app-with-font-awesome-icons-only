from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='This helps to pass variables using the cli')
parser.add_argument('--buildurl', action='store', type=str, help='Enters the build url')
args = parser.parse_args()
buildurl=args.buildurl


url=f"{buildurl}/consoleText"

#username = 'pocket'
#password = 'pocket'
api_token = '115e23f8ac223bc886e2be72c155a5f6cf'

#response=requests.get(url, auth=(username, password)).text

# Set up headers with API token
headers = {'Authorization': f'Bearer {api_token}'}


#response=requests.get(url, auth=(username, password)).text

# Make a request to the Jenkins job consoleText endpoint
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup=BeautifulSoup(response,'lxml')
    print(buildurl)
    print(soup.prettify())

# console_output=soup.find('pre',class_="console-output")
# print(console_output.text)
