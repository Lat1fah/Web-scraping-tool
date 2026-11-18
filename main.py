import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/" #set a variable to the URL you want to scrape

response = requests.get(URL) #sends a http get request to the URL we've pasted. the result will be stored in the response variable

print(response.status_code) #all requests have a status code 200 means its a success. 

soup = BeautifulSoup(response.content, "html.parser") #this line is fed the content and tell it which parser to use, in our case HTML(pythons builtin parser)
first_quote = soup.find("quote", class_="itemprop") #we use find to take 2 arguments to find the tag called quote and the classname called itemprop.the underscore on class_ ensures we can use a reserved word in python(class)
author= first_quote.span["author"]
tags = first_quote.find("k", class_="tags").text


#.\.venv\Scripts\Activate.ps1