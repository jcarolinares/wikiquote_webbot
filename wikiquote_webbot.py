# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests
import random
import sys

route="."
counter=0
after_name=False #Controls the order of the name: XXhXXm-nombre_archivo.gcode or nombre_archivo-XXhXXm.gcode
keywords_text=""


#Global variables
language={"spanish":"es","english":"en","italian":"it","polish":"pl","turkish":"tr","french":"fr","russian":"ru","german":"de","bulgarian":"bg","chinese":"zh"}
quotes=[]#The quotes container

print("WIKIQUOTE WEBBOT\n\n")

keywords=input("Please enter the keywords quote. You can enter different searchs adding a comma between searchs:\n")

keywords=keywords.split(",")

print("\n\nQUOTES\n")


#Functions
def print_quotes(number_of_quote):#Where -1 is all the quotes and -2 a random quote

    key_string=""
    for key_local in keywords:
        key_string=key_string+" "+key_local

    if number_of_quote==-1:
        for quote in quotes:
            print(quote+"\n\n"+"Quote about: "+str(key_string)+"\n\n")
    elif number_of_quote==-2:
        print(random.choice(quotes)+"\n\n"+"Quote about: "+str(key_string)+"\n\n")
    else:
        print(quotes[number_of_quote]+"\n\n"+"Quote about: "+str(key_string)+"\n\n")


for key in keywords:

    #Main script

    #Downloading the page
    r  = requests.get('http://'+language["english"]+'.wikiquote.org/wiki/'+key)
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
