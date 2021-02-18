# Amazon-produt-scrapping-using-python

This repository contains two different type of scrapping 
# 1st Method using Beautifulsoup
Using Beautifulsoup with the name of <b>Simple Scraper Using Python</b> that is completed by using a Jupyter Notebook, for this file you need to import three libararies by using the code below
import requests
from bs4 import BeautifulSoup
import sqlite3

First we will scrape any product by using it's url and after that we will save that product name,asin and the timestamp at the time of scrapping after that we will simply disply all the product by using product asin 

This code will use SQLite database that is easy to use with python and Jupyter. You have to just import the library and create the database. After that you will create the table and insert the records in that table. Finally, you will display the records. If you follow the notebook from the start you will not face any difficlty

# 2st Method using scrapy spider

This is very simple and fast method. Here we will use python library Scrapy that have many builtin functions.
You can use the bellow code for importing the library of Scrapy
import scrapy

We just scrape the product and display it. You can find it's code in the Spider folder. You have to make your own spider inside this foler and list the items in the items.py file that you are going to scrape for this case we just scrapping the name of Amazon product. But we can extend it as per our needs.


## Keep coding!
