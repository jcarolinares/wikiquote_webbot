# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests
import random


#Global variables
language={"spanish":"es","english":"en","italian":"it","polish":"pl","turkish":"tr","french":"fr","russian":"ru","german":"de","bulgarian":"bg","chinese":"zh"}
quotes=[]#The quotes container

print("WIKIQUOTE WEBBOT\n\n")

keywords=input("Please enter the keywords quote\n")
print("\n\nQUOTES\n")

#Functions
def print_quotes(number_of_quote):#Where -1 is all the quotes and -2 a random quote

    if number_of_quote==-1:
        for quote in quotes:
            print(quote+"\n\n"+"Quote about: "+keywords+"\n\n")
    elif number_of_quote==-2:
        print(random.choice(quotes)+"\n\n"+"Quote about: "+keywords+"\n\n")
    else:
        print(quotes[number_of_quote]+"\n\n"+"Quote about: "+keywords+"\n\n")


#Main script

#Downloading the page
r  = requests.get('http://'+language["spanish"]+'.wikiquote.org/wiki/'+keywords)
data = r.text
soup = BeautifulSoup(data,"lxml")

web_body=soup.find_all('div',class_="mw-content-ltr") #We take only the container of the quotes

list_of_quotes=web_body[0].find_all('li')

#Quotes
#for actual_quote in web_body:
for actual_quote in list_of_quotes:
	quotes.append(actual_quote.get_text())
	#print(actual_quote.get_text())

print_quotes(-1)
