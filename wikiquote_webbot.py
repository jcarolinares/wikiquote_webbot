# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests

print("WIKIQUOTE WEBBOT\n")

keywords=input("Please enter the keywords quote\n")
language={"spanish":"es","english":"en","italian":"it","polish":"pl","turkish":"tr","french":"fr","russian":"ru","german":"de","bulgarian":"bg","chinese":"zh"}


#Downloading the page
r  = requests.get('http://'+language["spanish"]+'.wikiquote.org/wiki/'+keywords)
data = r.text
soup = BeautifulSoup(data,"lxml")

#https://es.wikiquote.org/wiki/Madonna

web_body=soup.find_all('div',class_="mw-body-content")

#Quotes
quotes=[]
for actual_quote in web_body:
	quotes.append(actual_quote.get_text())
	print(actual_quote.get_text())

#<div id="bodyContent" class="mw-body-content">
