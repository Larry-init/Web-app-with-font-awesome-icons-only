from bs4 import BeautifulSoup
import requests

url='http://192.168.43.247:8080/job/Web-app-with-font-awesome-icons-only/job/master/10/console'
username = 'pocket'
password = 'pocket'

url=requests.get(url, auth=(username, password)).text

soup=BeautifulSoup(url,'lxml')
console=soup.find('pre',class_='console-output').text
print(console)