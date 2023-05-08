from bs4 import BeautifulSoup

with open("index.html") as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")
# Udělá list všech odkazů
all_a = soup.find_all("a")
print(all_a)

for one_a in all_a:
    # nebo místo string napsat gettext
    # print(one_a.string)

    # Printuje jen odkazy
    print(one_a.get("href"))
