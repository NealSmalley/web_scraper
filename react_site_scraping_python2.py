import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "http://byu-studies-frontend.s3-website-us-west-2.amazonaws.com/article/5"

session = HTMLSession()
response = session.get(url)
response.html.render(sleep=.5)

soup = BeautifulSoup(response.html.html, 'html.parser')
books = soup.find(class_='text-lg article lg:min-w-[700px] pb-10')
print(books.text)