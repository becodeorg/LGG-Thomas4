import requests
import json

root_url = "https://newsapi.org/v2"
endpoint = "top-headlines" 
params = {
    "apiKey": "73bbb95f8ecb49b499113a46481b4af1",
    "sources": "lequipe"
}

# call the get method of requests on our specifications
response = requests.get(f"{root_url}/{endpoint}", params=params)


print(json.dumps(response.json(), indent=4))