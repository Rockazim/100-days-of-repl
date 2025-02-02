import requests
from bs4 import BeautifulSoup
import requests, json, os
from openai import OpenAI


url = input("Paste wiki article ")
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
myLinks = soup.find_all("p")
reference = soup.find_all("ol", {"class":"references"})

article = ""

for link in myLinks:
    article += link.text


#https://platform.openai.com/settings/organization/api-keys
openai_api_key = "YOURAPIKEY"

client = OpenAI(
  api_key= openai_api_key
)
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": f"Summarize this in less than 3 paragraphs {article}"}
    ]
)

response = completion.choices[0].message
better_response = response.content

print(f"{better_response}\n")
print("Sources")
for x in reference:
    print(x.text)
