# The selenium.webdriver module provides all the implementations of WebDriver
# Currently supported are Firefox, Chrome, IE and Remote. The `Keys` class provides keys on
# the keyboard such as RETURN, F1, ALT etc.
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # Here, we create instance of Firefox WebDriver.
# driver = webdriver.Firefox()

# # The driver.get method will lead to a page given by the URL. WebDriver will wait until the page is fully
# # loaded (i.e. the "onload" event has been triggered) before returning the control to your script.
# # It should be noted that if your page uses a lot of AJAX calls when loading, WebDriver may not know
# # when it was fully loaded.
# driver.get("http://www.python.org")

# # The following line is a statement confirming that the title contains the word "Python".
# assert "Python" in driver.title

# # WebDriver offers a method `find_element` that aims to search for item based on attributes
# # For example, the input text element can be located by its name attribute by
# # using the attribute `name` with the value `q`
# elem = driver.find_element(By.NAME, "q")

# # Then we send keys. This is similar to entering keys using your keyboard.
# # Special keys can be sent using the `Keys` class imported in line 7 (from selenium.webdriver.common.keys import Keys).
# # For security reasons, we will delete any pre-filled text in the input field
# # (for example, "Search") so that it does not affect our search results:
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

# # After submitting the page, you should get the result if there is one. To ensure that certain results
# # are found, make an assertion that ensures that the source page does not contain the word "No results found".
# assert "No results found." not in driver.page_source
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Chemin vers geckodriver
# service = Service('C:/geckodriver/geckodriver.exe')

# # Options Firefox
# options = Options()
# options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'  # Spécifiez le chemin vers l'exécutable Firefox
# # options.add_argument('--headless')  # Facultatif : exécution en mode headless (sans interface graphique)

# # Initialiser le navigateur
# driver = webdriver.Firefox(service=service, options=options)

# try:
#     url = "https://www.nytimes.com/"
#     driver.get(url)

#     # Attendre que le bouton d'acceptation des cookies soit cliquable
#     wait = WebDriverWait(driver, 5)
#     cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='Accept all-btn']")))
#     cookie_button.click()

#     article_titles = driver.find_elements(By.XPATH, "//section[@class='story-wrapper']//p[@class='indicate-hover css-1a5fuvt'] | //p[@class='indicate-hover css-1gg6cw2']")

#     all_titles = []
#     for title in article_titles:
#         all_titles.append(title.text)

#     print(all_titles)


# finally:
#     # Fermer le navigateur
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chemin vers geckodriver
service = Service('C:/geckodriver/geckodriver.exe')

# Options Firefox
options = Options()
options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'  # Spécifiez le chemin vers l'exécutable Firefox
# options.add_argument('--headless')  # Facultatif : exécution en mode headless (sans interface graphique)

# Initialiser le navigateur
driver = webdriver.Firefox(service=service, options=options)

try:
    url = "https://www.sudinfo.be/2098/sections/regions/liege"
    driver.get(url)

    # Attendre que le bouton d'acceptation des cookies soit cliquable
    wait = WebDriverWait(driver, 5)
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='didomi-notice-agree-button']")))
    cookie_button.click()

    article_titles = driver.find_elements(By.XPATH, "//a[@class='r-article--link']")

    all_titles = []
    for title in article_titles:
        all_titles.append(title.text)

    print(all_titles[0])


finally:
    # Fermer le navigateur
    driver.quit()



    
