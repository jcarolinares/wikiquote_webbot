# Wikiquote_webbot
A little program that makes scraping from wikiquote showing quotes from a search.

The program uses BeautifulSoup and Python 3. You can find more info of this amazing library in:

[https://www.crummy.com/software/BeautifulSoup/]

** HOW TO PUT A QUOTE EVERY TIME YOU OPEN A NEW TERMINAL **

1-Put the file "terminal_wikiquote_webbot.py" in your HOME directory

2-Open a new terminal and in the HOME directory open this file:

``` bash

gedit .bashrc

```

Don't change the file, just add a new line at the end of the file that execute the program and the quote keywords, one example:

```

python3 terminal_wikiquote_webbot.py Terry Pratchett

```

Every time you'll open a new terminal, the program will show a random quote based in the given keywords

You can also put a mix of different search quotes, just put commas between the different theme quote. As an example:

```

python3 terminal_wikiquote_webbot.py Terry Pratchett, Asimov

```

The terminal will put a random quote about Terry Pratchett or Asimov



Made by Julián Caro Linares

jcarolinares@gmail.com

CC-BY-SA
