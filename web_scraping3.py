from bs4 import BeautifulSoup

with open("index.html") as file:
    read = file.read()
    soup = BeautifulSoup(read, "html.parser")
    all_a = soup.find_all("a")

with open("Output/linky.txt", mode="a") as linky:
    for one_a in all_a:
        linky.write(str(one_a.get("href")))
        linky.write("\n")

file.close()
linky.close()
