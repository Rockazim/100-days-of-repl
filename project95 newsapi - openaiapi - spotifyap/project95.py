import requests, json, os
from openai import OpenAI
import time
from requests.auth import HTTPBasicAuth

#https://newsapi.org/account
newsKey = "YOUR API KEY"
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"
response = requests.get(url)
data = response.json()
i = 0
results = []
for x in data['articles']:
    results.append(x['title'])
    i += 1
    if i ==5:
        break
#https://platform.openai.com/settings/organization/api-keys
openai_api_key = "YOUR SECRET API KEY"

client = OpenAI(
  api_key= openai_api_key
)


completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": f"Write only two to three words to summarize each headline {results}"}
    ]
)
headlines = []
realheadlines = []


response = completion.choices[0].message
better_response = response.content
headlines = better_response.split(".")
for x in headlines:
    if headlines[-1] != x:
        realheadlines.append(x[:-3])
    else:
        realheadlines.append(x)

del realheadlines[0]



#https://developer.spotify.com/dashboard/66448860640c4fe9a84543f8f666b9ad/settings
clientID = "YOUR CLIENT ID"
clientSecret = "YOUR CLIENT SECRET"
url = 'https://accounts.spotify.com/api/token'
data = {'grant_type': 'client_credentials'}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(url, data=data, auth=auth)
accessToken = response.json()['access_token']
real_url = 'https://api.spotify.com/v1/search'
headers = {'Authorization': f'Bearer {accessToken}'}

for x in range(len(realheadlines)):
    name = realheadlines[x]
    search = f'?q={name}&type=track&limit=1'
    fullURL = f'{real_url}{search}'
    response = requests.get(fullURL, headers=headers)
    data = response.json()
    for track in data['tracks']['items']:
        song_name = track["name"]
        print(name.strip() )
        print(song_name)
        song_link = track["external_urls"]["spotify"]
        print(song_link)
        print()
