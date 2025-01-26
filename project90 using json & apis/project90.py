import requests, json

for i in range(10):
    result = requests.get("https://randomuser.me/api/")
    user = result.json()
    first_name = user["results"][0]["name"]["first"]
    last_name = user["results"][0]["name"]["last"]
    image = user["results"][0]["picture"]["medium"]
    
    picture = requests.get(image)
    
    f = open(f"{first_name} {last_name}.jpg", "wb")
    f.write(picture.content)
    f.close()