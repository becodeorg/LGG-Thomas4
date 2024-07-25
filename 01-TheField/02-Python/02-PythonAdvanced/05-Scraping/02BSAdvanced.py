from bs4 import BeautifulSoup
import requests
import pandas as pd

data = {
    'Title': [],
    'Synopsis': [],
    'Links': []
}

url = "http://www.allocine.fr"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

links = []
for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    links.append(elem.get("href"))

movie_links = [url + elem for elem in links if "film" in elem]


for i in movie_links:
    r = requests.get(i)
    data['Links'].append(i)

    soup = BeautifulSoup(r.content, "html.parser")

    title = soup.find_all("div", attrs={"titlebar-title titlebar-title-xl"})
    data['Title'].append(title[0].text)

    for elem in soup.find_all("section", attrs={"id": "synopsis-details"}):
        for elem2 in elem.find_all("div", attrs={"class":"content-txt"}):
            data['Synopsis'].append(elem2.text.strip())

df = pd.DataFrame(data)

csv_file_path = './assets/allo_cine.csv'
df.to_csv(csv_file_path, index=False)

print("done !")

