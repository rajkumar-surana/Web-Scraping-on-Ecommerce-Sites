from bs4 import BeautifulSoup as soup
import pandas as pd
from urllib.request import urlopen as uReq
#driver = webdriver.Chrome()
my_url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers= page_soup.findAll("div",{"class": "_1UoZlX"})
#print(len(containers))

#print(soup.prettify(containers[0]))
#container=containers[0]
#print(container.a.div.img["alt"])
#price=container.findAll("div",{"class": "col col-5-12 _2o7WAb"})
#print(price[0].text)


#uncommenting above line will print data on  screen so to print abouve lines and comment below lines.
filename="products_flipkart.csv"
f=open(filename,"w")
header="product,pricing \n"
f.write(header)
for container in containers:
    product_name=container.div.img["alt"]
    price_container=container.findAll("div",{"class": "col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()
    
    print(product_name)
    print(price)
    f.write(product_name+"   ,     "+price+"\n")
    #print(strike_price)
    
    
f.close()
