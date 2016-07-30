# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests
import random
import sys

class quote:
    def new(self,about,content):
        self.about=about
        self.content=content

    def show_quote(self):
        print (self.content+"\n")
        print("Quote about: "+self.about+"\n\n")

keywords_text=""


#Terminal parameter
if __name__ == '__main__':

    #print(len(sys.argv))

    if len(sys.argv) >= 1:
        list_keywords=sys.argv
        #list_keywords.remove("terminal_wikiquote_webbot.py")
        list_keywords.pop(0)


        for element in list_keywords:
            keywords_text=keywords_text+" "+str(element)

#print (keywords_text)
keywords=keywords_text

#Global variables
language={"spanish":"es","english":"en","italian":"it","polish":"pl","turkish":"tr","french":"fr","russian":"ru","german":"de","bulgarian":"bg","chinese":"zh"}
quotes_objects=[]#The quotes containerr

#print("WIKIQUOTE WEBBOT\n\n")

#keywords=input("Please enter the keywords quote\n")
#print("\n\nQUOTES\n")
keywords=keywords.split(",")

#print("\n\nQUOTES\n")


#Functions
def print_quotes(number_of_quote):#Where -1 is all the quotes and -2 a random quote

    key_string=""
    for key_local in keywords:
        key_string=key_string+" "+key_local

    if number_of_quote==-1:
        for quote in quotes_objects:
            quote.show_quote()
    elif number_of_quote==-2:
        random.choice(quotes_objects).show_quote()
    else:
        quotes_objects[number_of_quote].show_quote()


#Main script
for key in keywords:

    #Downloading the page
    r  = requests.get('http://'+language["english"]+'.wikiquote.org/wiki/'+key)
    data = r.text
    soup = BeautifulSoup(data,"lxml")

    web_body=soup.find_all('div',class_="mw-content-ltr") #We take only the container of the quotes

    list_of_quotes=web_body[0].find_all('li')

    #Quotes
    #for actual_quote in web_body:
    for actual_quote in list_of_quotes:
        auxiliar_object=quote()
        auxiliar_object.new(key,actual_quote.get_text())
        quotes_objects.append(auxiliar_object)
        #auxiliar_object.show_quote()

print_quotes(-2)
