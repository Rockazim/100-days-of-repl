from flask import Flask, request
from requests.auth import HTTPBasicAuth
import requests, json, os

app = Flask(__name__)

clientID = "INPUTCLIENTID"
clientSecret = "INPUTCLIENTSECRET"
url = 'https://accounts.spotify.com/api/token'
data = {'grant_type': 'client_credentials'}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(url, data=data, auth=auth)
accessToken = response.json()['access_token']
url = 'https://api.spotify.com/v1/search'
headers = {'Authorization': f'Bearer {accessToken}'}

@app.route('/', methods=['GET', 'POST'])
def main():
    page = ""
    test = ""
    if request.method == "POST":
        year = request.form["year"]
        search = f'?q=year%3A{year}&type=track&market=ES&limit=10&include_external=audio'
        fullURL = f'{url}{search}'
        response = requests.get(fullURL, headers=headers)
        data = response.json()

        g = open("html/replacedform.html", "r")
        better_page = g.read()
        g.close()
        for track in data['tracks']['items']:
            song_name = track["name"]
            song_link = track["external_urls"]["spotify"]

            new_page = better_page
            new_page = new_page.replace("{content}", song_name)
            new_page= new_page.replace("{song}", song_link)
            test += new_page

    f = open('html/form.html', 'r')
    page = f.read()
    f.close()
    
    return page + test 

app.run(host='0.0.0.0', port=81)
