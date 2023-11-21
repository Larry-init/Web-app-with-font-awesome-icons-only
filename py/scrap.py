from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='This helps to pass variables using the cli')
parser.add_argument('--buildurl', action='store', type=str, help='Enters the build URL')
args = parser.parse_args()
buildurl = args.buildurl

print(buildurl)

url = f"{buildurl}/console"
print(url)

username = 'pocket'
password = 'pocket'

try:
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    console_element = soup.find('pre', class_='console-output')

    if console_element:
        console = console_element.text
        print(console)
    else:
        print("Console output not found.")
except requests.RequestException as e:
    print(f"Error: {e}")
