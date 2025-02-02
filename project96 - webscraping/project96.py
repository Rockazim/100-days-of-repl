import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
myLinks = soup.find_all( "a")
print(len(myLinks))


for link in myLinks:
    if 'Python' in link.text:
        print(link.text)
    elif 'Replit' in link.text:
        print(link.text)
