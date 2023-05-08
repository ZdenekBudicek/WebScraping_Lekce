from bs4 import BeautifulSoup

with open("index.html") as file:
    html_code = file.read()
    # Tím html.parser mu říkám že bude analizovat kód v html
soup = BeautifulSoup(html_code, "html.parser")
# nadpis
print(soup.title)
# vypíše název tagu (title)
print(soup.title.name)
# vypíše čistě nadpis
print(soup.title.string)

# p první odstavec
print(soup.p)
print(soup.p.string)

# a hledá první odkaz
print(soup.a)
print(soup.a.name)
