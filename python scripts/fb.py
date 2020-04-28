from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import re


# https://www.amazon.ca/s?k= search for amazon
# https://www.newegg.ca/p/pl?d= search for newegg
url = "https://www.newegg.ca/p/pl?d=intel+core+i5"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = bs(page_html, "html.parser")
list_wrap = page_soup.find("div", {"class":"list-wrap"})
containers = list_wrap.findAll("div", {"class": "item-container"})

filename = "products_newegg.csv"
f = open(filename, "w")
headers = "title, price\n"
f.write(headers)
for container in containers:
    title_containers = container.findAll("a", {"class":"item-title"})
    price_containers = container.findAll("li", {"class":"price-current"})
    # print(title_containers[0].text)
    # print(price_containers[0].text.strip()[0: len(price_containers[0].text.strip())-1].strip())
    # print(price_containers[0].text[0, len(price_containers[0].text)-1].strip())
    title = title_containers[0].text.replace(",", "|")
    price = price_containers[0].text.strip()[0: len(price_containers[0].text.strip())-1].strip()
    price = re.search('\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})', price)
    price = price.group(0)
    f.write(title + "," + price + "\n")

f.close()
