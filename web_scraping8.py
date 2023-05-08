from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.seznam.cz/")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(class_="article__title")

with open("Output/seznam.txt", "w") as file:
    for one_article in articles:
        one_article_text = one_article.getText()
        one_article_link = one_article.get("href")
        # Nadpis
        # print(one_article_text)
        # Odkaz
        # print(one_article_link)

        # Hledá slovo Covid v nějakém nadpisu článku
        if "Covid" in one_article_text:
            print(one_article_text)
            print(one_article_link)

            file.write(one_article_text)
            file.write("\n")
            file.write(one_article_link)
