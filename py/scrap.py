from bs4 import BeautifulSoup
import requests
import argparse
import sys

parser = argparse.ArgumentParser(description='This helps to pass variables using the CLI')
parser.add_argument('--buildurl', action='store', type=str, help='Enters the build URL')
args = parser.parse_args()
buildurl = args.buildurl

url = f"{buildurl}/console"

username = 'pocket'
password = 'pocket'

try:
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()  # Check for HTTP errors
    soup = BeautifulSoup(response.text, 'lxml')
    console = soup.find('pre', class_='console-output').text
    print(console)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
