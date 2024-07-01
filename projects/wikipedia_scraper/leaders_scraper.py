import requests
from bs4 import BeautifulSoup
import re
from requests import Session
import json


def get_first_paragraph(wikipedia_url: str, session: Session) -> str:
   response = session.get(wikipedia_url)
   soup = BeautifulSoup(response.text, 'html.parser')
   for tag in soup.find_all("p"):
      if '<b>' in str(tag) and len(str(tag)) > 60:
         first_paragraph = tag.text
         break
   first_paragraph = re.sub(r"\xa0", ' ', first_paragraph, flags=re.IGNORECASE)
   for pattern in [r"\n", r"\[\d+\]", r"\[n\s\d+\]", r"\sÉcouter", r"\(uitspraakⓘ\)\s", r"uitspraakⓘ\s", r"\[\w\]", r"\s\[.+\]", r"ⓘ", r"/.+/;"]:
      first_paragraph = re.sub(
          pattern, '', first_paragraph, flags=re.IGNORECASE)
   return first_paragraph


def get_leaders() -> dict:
    url = "https://country-leaders.onrender.com"
    cookie_url = "/cookie"
    countries_url = "/countries"
    leaders_url = "/leaders"
    cookie_req = requests.get(url + cookie_url)
    cookie = cookie_req.cookies
    countries = requests.get(url + countries_url, cookies=cookie).json()
    leaders_dictionany = {c: requests.get(
        url + leaders_url, cookies=cookie, params={'country': c}).json() for c in countries}
    for c in countries:
        urls = [item['wikipedia_url'] for item in leaders_dictionany[c]]
        with Session() as session:
            for i in range(len(urls)):
                leaders_dictionany[c][i] = get_first_paragraph(
                    urls[i], session)
    return leaders_dictionany


leaders_per_country = get_leaders()


def save(dict_name: dict, filename='leaders'):
    with open(filename + '.json', 'w') as fp:
        json.dump(dict_name, fp)


save(leaders_per_country)