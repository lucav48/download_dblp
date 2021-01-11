from bs4 import BeautifulSoup
import requests

journal = "isr"
url = "https://dblp.uni-trier.de/db/journals/" + journal + "/"
html_page = requests.get(url)
soup = BeautifulSoup(html_page.text, 'html.parser')
link_list = []
print("Journal: " + journal)
for link_elem in soup.findAll('a'):
    link = link_elem.get('href')
    if link and url in link:
        link_list.append(link)
print("Found : " + str(len(link_list)) + " link to follow")

article_name = []
for link in link_list:
    html_page = requests.get(link)
    soup = BeautifulSoup(html_page.text, 'html.parser')
    for link_elem in soup.findAll('span', attrs={"class":"title", "itemprop":"name"}):
        article_name.append(link_elem.text)
print("Found : " + str(len(article_name)) + " articles")
filename = "journal/" + journal + ".txt"
f = open(filename, "w", encoding="utf-8")
print("Writing them to " + filename)
for art in article_name:
    f.write(art + "\n")
f.close()
