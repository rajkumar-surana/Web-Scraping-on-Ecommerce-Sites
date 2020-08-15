from bs4 import BeautifulSoup as soup
import pandas as pd
from urllib.request import urlopen as uReq
#driver = webdriver.Chrome()
basic_url="https://www.jiomart.com/c/groceries/dairy-bakery/dairy/62" # pls have your exact link here and at below line with comment.
page=1
my_url=basic_url
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
infos=page_soup.find("span",{"id":"total_count"})
print(infos.text)
print(infos)
length=int(infos.text)
containers=list()

containers= page_soup.findAll("div",{"class": "col-md-3 p-0"})

#print(soup.prettify(containers[0]))
#container=containers[0]
#print(container.a.div.img["alt"])
#price=container.findAll("div",{"class": "col col-5-12 _2o7WAb"})
#print(price[0].text)
filename="products_jio.csv"
f=open(filename,"w")
header="product    ,                strike_price     ,     price \n"
f.write(header)

print(len(containers))
for container in containers:
    product_name_container=container.findAll("span",{"class": "clsgetname"})
    product_name=product_name_container[0].text.strip()
    strike_price_container=container.findAll("strike",{"id": "price"})
    strike_price=strike_price_container[0].text.strip()
    price_container=container.findAll("span",{"id":"final_price"})
    price=price_container[0].text
    #str=""
    #str=str.join(price)
    
    print(product_name)
    print(strike_price)
    print(price)
    f.write(product_name+"   ,   "+strike_price+"   ,   "+price+"\n")

page=1
print("page 1 completed")
while(length>20):
    page=page+1
    print("page set to 2")
    length=length-20
    mod_url="https://www.jiomart.com/c/groceries/dairy-bakery/dairy/62/page/{}" #have your link before /page
    my_url=mod_url.format(page)
    print(my_url)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    containers= page_soup.findAll("div",{"class": "col-md-3 p-0"})
    
    for container in containers:
        product_name_container=container.findAll("span",{"class": "clsgetname"})
        product_name=product_name_container[0].text.strip()
        strike_price_container=container.findAll("strike",{"id": "price"})
        strike_price=strike_price_container[0].text.strip()
        price_container=container.findAll("span",{"id":"final_price"})
        price=price_container[0].text
    
        print(product_name)
        print(strike_price)
        print(price)
        f.write(product_name+"   ,   "+strike_price+"   ,   "+price+"\n")
    
    
    
    
f.close()

    
