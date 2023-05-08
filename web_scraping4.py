from bs4 import BeautifulSoup

with open("index.html") as file:
    read = file.read()

soup = BeautifulSoup(read, "html.parser")

heading = soup.find(name="h1", id="name")
print(heading)
#                               class se musí psát s podtržítkem, aby to nebylo class z OOP
heading2 = soup.find(name="h2", class_="about")
print(heading2)

about = soup.find_all(class_="about")
print(about)
#                       všechny linky uložené v odstavci
contact = soup.select_one("p a")
print(contact)
