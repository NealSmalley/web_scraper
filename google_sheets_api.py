import os
from web_scraper.Google import Create_Service

CLIENT_SECRET_FILE = "client_secret_416758173161-2csk8bcnqnatq4874vseqh048g46qdi0.apps.googleusercontent.com.json"
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)