import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

my_url = "http://www.dealsource.tech/"

# openning the connection, grabbing the page.
client = urlopen(my_url)
page_html = client.read()
client.close()

# HTML Parsing.
page_soup = soup(page_html, "html.parser")

# list of containers.
containers = page_soup.findAll("div", {"class":"summary-item"})

# Openning a csv file.
filename = "products.csv"
f = open(filename, "w")
headers = "product_name, ex_price, new_price, year, month, day\n"
f.write(headers)

# grabbing title, ex, new price and date for each product, then save info to products.csv
for container in containers:
    product_name = container.div.a["data-title"]
    ex_price = container.find("div", {"class":"summary-excerpt"}).text.split(" ")[1]
    new_price = container.find("div", {"class":"summary-excerpt"}).text.split(" ")[-1]
    date = container.find("div", {"class":"summary-content sqs-gallery-meta-container"}).time["datetime"].split("-") 
    f.write(product_name.replace(",", "|") + "," + ex_price + "," + new_price + "," + date[0] + "," + date[1] + "," + date[-1] + "\n")
# Closing...
f.close()
