from bs4 import BeautifulSoup
import requests

# Nejdříve potřebujeme požádat o přístup
response = requests.get("http://www.ekospace.cz/")

# Zde po tom co máme přístup ho převedeme na obsah (text)
web = response.text

# klasika plugin a pak obsah a pak že to je html kód
soup = BeautifulSoup(web, "html.parser")
text_book = soup.find(name="a", class_="ucebnice ucebniceMakro")
pdf = text_book.get("href")

url = "http://www.ekospace.cz/"

# Musíš spojit základní stránku + ten odkaz na soubor
pdf_url = url + pdf

# Žádost o adresu na stažení souboru
response2 = requests.get(pdf_url)
#         do složky Output mi vytvoř wordovej soubor a bude binárně zapsanej (to je to wb)
with open("Output/neco.doc", "wb") as file:
    # stáhni content z žádosti toho webu (což je daný soubor)
    file.write(response2.content)
