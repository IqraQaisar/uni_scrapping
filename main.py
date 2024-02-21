import requests 
from bs4 import BeautifulSoup

response = requests.get("https://www.aiou.edu.pk/")
#print(response.content)
soup=BeautifulSoup(response.content,"html.parser")
#finding title of the page
print(soup.title.string)
#find and print all links
for link in soup.find_all("a"):
    print(link.get("href"))

