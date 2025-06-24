import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Product_Price = []
Reviews = []


for i in range(2,8):	
	#import url
	url = "https://www.flipkart.com/search?q=new+mobail&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"+str(i)

	r = requests.get(url)

	# import all html page
	soup = BeautifulSoup(r.content, "html.parser")

	# import html page selected box 
	box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

	# import Product name with box function
	names = box.find_all("div", class_ = "_4rR01T")

	#print(names)

	for i in names:
		name = i.text
		#print(name)
		Product_name.append(name)
	print(len(Product_name))



	# import Reviews with box function used
	reviews = box.find_all("div", class_="_3LWZlK")

	for i in reviews:
		rev = i.text
		Reviews.append(rev)
	print(len(Reviews))


	# import Product_Price with box function used
	price = box.find_all("div", class_ = "_30jeq3 _1_WHN1")

	for i in price:
		price = i.text
		Product_Price.append(price)
	print(len(Product_Price))
	#print(Product_Price)

#print(Product_name)
#print(Product_Price)
#print(Reviews)

#df = pd.DataFrame({"Product_name" : Product_name, "Product_Price" : Product_Price, "Reviews" : Reviews}, dtype={"Product_name" : str, "Product_Price" : str, "Reviews" : str})
df = pd.DataFrame({"Product_name" : Product_name, "Product_Price" : Product_Price, "Reviews" : Reviews})

print(df)
#df.to_csv("C:/Users/cheta/Desktop/Python/Flipcart Web Scraping/Flipcart_new_mobail.csv")