import requests
from bs4 import BeautifulSoup

# URL à récupérer
url = 'https://webscraper.io/test-sites/e-commerce/allinone'   # Remplacez par l'URL de votre choix

# Récupérer le contenu de l'URL
response = requests.get(url)
content = response.content

# Parser le contenu avec BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Obtenir tous les h1
h1_tags = soup.find_all('h1')
h1_contents = [h1.text for h1 in h1_tags]

# Obtenir le premier h2

h2_tags = soup.find_all('h2')
h2_contents = [h2.text for h2 in h2_tags]

# Obtenir le premier paragraphe

p_tags = soup.find_all('p')
p_contents = [p.text for p in p_tags]


# Afficher l'arborescence
print("Arborescence du contenu de la page :")

for i, h1_content in enumerate(h1_contents, start=1):
    print(f"H1 tag {i}: {h1_content.strip()}")


for i, h2_content in enumerate(h2_contents, start=1):
    print(f"H2 tag {i}: {h2_content.strip()}")


for i, p_content in enumerate(p_contents, start=1):
    print(f"P  tag {i}: {p_content.strip()}")

