import requests, json, os
from openai import OpenAI
import time
newsKey = "YOUR API KEY"
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"




openai_api_key = "YOUR API KEY"

client = OpenAI(
  api_key= openai_api_key
)


result = requests.get(url)
data = result.json()
i = 1
results = []

for article in data["articles"]:
    headline = f'Author: {article['author']} Title: {article['title']} Description: {article['description']}'
    results.append(headline)
    if i == 5:
        break
    else:
        i+= 1


completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": f"Write a short summary for each news article {results}"}
    ]
)

response = completion.choices[0].message
print(response.content)
