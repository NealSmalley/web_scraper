import webbrowser
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re
import csv
import queue
import time
import random
from requests_html import HTMLSession
import os
from openai import OpenAI

#opens all urls
#5618
for i in range(5452, 5618):
    i = str(i)
    url = "http://byu-studies-frontend.s3-website-us-west-2.amazonaws.com/article/"+i
    #webbrowser.open(url)

#scrapes the page
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=.5)

    soup = BeautifulSoup(response.html.html, 'html.parser')
    article = soup.find(class_='text-lg article lg:min-w-[700px] pb-10')
    article_text = article.text

#chatgpt api to find scriptures
    content = article_text

# Function to read the API key from the secret file
    def get_api_key_from_file(file_path='secret.txt'):
        try:
            with open(file_path, 'r') as file:
                # Read the first line where the API key is expected to be
                api_key = file.readline().strip()
                return api_key
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return None

# Retrieve the API key from the secret.txt file
    api_key = get_api_key_from_file()

    if not api_key:
        print("API Key not found. Please ensure your API key is in secret.txt.")
        exit()

# Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)

# Example usage of the client to create a chat completion
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Can you find if there are any scripture references in this text and if there are scriptures include all the scriptures but not the verses?" + content,
                }
            ],
            model="gpt-3.5-turbo",
        )
        # Print the response
        print(chat_completion.choices[0].message.content)
        print("response")
        i = int(i)
        i = i + 1
        with open('final_webcrawler2.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([chat_completion.choices[0].message.content])
            writer.writerow(["+"])
            writer.writerow([i])
    except Exception as e:
        print(f"An error occurred: {str(e)}")