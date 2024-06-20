import requests
import re
import json
from bs4 import BeautifulSoup

def get_leaders():
    root_url = 'https://country-leaders.onrender.com'
    countries_url = root_url + '/countries'
    leaders_url = root_url + '/leaders'
    cookie_url = root_url + '/cookie'
    cookies = requests.get(cookie_url).cookies
    countries = requests.get(countries_url, cookies=cookies).json()
    
    leaders_per_country = {}
    session = requests.Session()
    for country in countries:
        country_leaders = requests.get(leaders_url, cookies=cookies, params={"country": country}).json()
        for leader in country_leaders:
            wikipedia_url = leader.get('wikipedia_url')
            leader["biography"] = get_first_paragraph(wikipedia_url, session)
        leaders_per_country[country] = country_leaders
    return leaders_per_country

def get_first_paragraph(wikipedia_url, session):
    output_html = session.get(wikipedia_url).text
    soup = BeautifulSoup(output_html, features="html.parser")
    all_paragraphs_page = soup.find_all('p')
    for paragraph in all_paragraphs_page:
        if paragraph.find('b') or paragraph.find('strong'):
            first_paragraph = paragraph.get_text()
    cleaned_first_paragraph = re.sub(r'\[\d+\]|\([^)]*?\ⓘ[^)]*?\)|<[^>]*>|\(/[^)]+\)|\([^()]*?/[^()]*?\)|\n$', '', first_paragraph)
    return cleaned_first_paragraph

def save(updated_leaders, output_file="leaders.json"):
    with open(output_file, "w") as file:
        json.dump(updated_leaders, file, indent=4)
        
leaders_per_country = get_leaders()
save(leaders_per_country)