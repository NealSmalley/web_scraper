import webbrowser
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re
import csv
import queue
import time
import random



i = str(5)
#url = "http://byu-studies-frontend.s3-website-us-west-2.amazonaws.com/article/"+ i
webbrowser.open("http://byu-studies-frontend.s3-website-us-west-2.amazonaws.com/article/"+i)
#print(url)
#page = requests.get(url)
#print(page)
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
#text = soup.find(class_="text-left")
#print(text_content)

#for i in range(4, 5618):
#    i = str(i)
#    webbrowser.open("http://byu-studies-frontend.s3-website-us-west-2.amazonaws.com/article/"+i)