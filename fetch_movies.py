import os
import requests
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('TMDB_READ_ACCESS_TOKEN')
api_key = os.getenv('TMDB_API_KEY')

def createNewRequestToken():
    url = "https://api.themoviedb.org/3/authentication/token/new"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    if response == 200:
        return response.text
    else:
        return response.text

  

