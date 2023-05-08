from bs4 import BeautifulSoup

with open("info.html") as file:
    read = file.read()

soup = BeautifulSoup(read, "html.parser")

heading = soup.title.text
print(heading)

heading2 = soup.find(name="h2").text
print(heading2)

ul = soup.find_all("ul")
for history_list in ul:
    print(history_list.text)

all_p = soup.find_all("p")
print(all_p)
for one_all_p in all_p:
    print(one_all_p)

for one_all_p in all_p:
    print(one_all_p.text)

all_a = soup.find_all("a")
print(all_a)
for one_a in all_a:
    print(one_a)

for one_a in all_a:
    print(one_a.text)

for one_a in all_a:
    print(one_a.get("href"))
