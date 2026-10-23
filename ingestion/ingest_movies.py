import os
import requests
import time
from dotenv import load_dotenv
import json

load_dotenv()

access_token = os.getenv('TMDB_READ_ACCESS_TOKEN')
api_key = os.getenv('TMDB_API_KEY')
base_url = "https://api.themoviedb.org/3"

# def createNewRequestToken():
#     url = "https://api.themoviedb.org/3/authentication/token/new"
#     headers = {
#         "accept": "application/json",
#         "Authorization": f"Bearer {access_token}"
#     }
#     response = requests.get(url, headers=headers)
#     if response == 200:
#         return response.text
#     else:
#         return response.text

# Headers, url and params

# Ingest Popular movies and handle retryable errors
# RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
# def get_with_retry(url, headers, params, max_retries=3):
#     for attempt in range(max_retries + 1):
#         try:
#             response = requests.get(
#                 url, 
#                 headers=headers, 
#                 params=params, 
#                 timeout=(5,30))
                
#             # Retry HTTP errors
#             retry_after = response.headers.get("Retry-After")
    
#             if response.status_code in RETRYABLE_STATUS_CODES:
#                 if attempt == max_retries:
#                     response.raise_for_status()
#                     # The errors will be ignored three times and if they happen more than three times then the error will be presented
        
#                 if retry_after and retry_after.isdigit(): # if there is a numerical retry_after in the get request header
#                     wait_seconds = min(int(retry_after), 120)
#                 else:
#                     wait_seconds = 2 ** attempt # Exponential backoff
    
#                 print(
#                     f"HTTP {response.status_code}."
#                     f"Retrying in {wait_seconds}s..."
#                 )
#                 time.sleep(wait_seconds)
#                 continue
    
#             # Raise errors such as 400, 401, 403, 404
#             response.raise_for_status()
    
#             return response.json()
#         except (
#             requests.exceptions.Timeout,
#             requests.exceptions.ConnectionError
#         ) as e:
#             if attempt == max_retries:
#                 raise
    
#             wait_seconds = min(2 ** attempt, 30)
#             print(
#                 f"{type(e).__name__}."
#                 f"Retrying in {wait_seconds}s..."
#             )
#             time.sleep(wait_seconds)
    
#     raise RuntimeError("Request failed after all retries ")

# def getPopularMovies(max_pages=20):
#     page = 1
#     movies = []
#     # Handle problems with the access token
#     if not access_token:
#         raise ValueError("The access token has not been read.")

#     try:
#         while page <= max_pages:
#             print(f"Requesting page {page}...")

#             data = get_with_retry(
#                 url,
#                 headers,
#                 params = {"language": "en-US", "sort_by": "popularity.desc", "page": page}

#             )
#             # Add to db

#             page_movies = data.get("results, []")
#             movies.append(page_movies)

#             print(
#                 f"Page {page} completed."
#                 # f"Records fetched: {len(page_movies)}"
#             )
#             # Check if there are anymore pages. If not then the while loop will stop
#             if not page_movies or page >= data["total_pages"]:
#                 break
#             page += 1
#     except requests.exceptions.HTTPError as e:
#         status = e.response.status_code if e.response else "unknown"
#         print(f"HTTP {status}: ingestion stopped at page {page}")

#     

#     print(f"Total records collected: {len(movies)}")
#     print(f"{movies}")

def getPopularMovies(url, headers, page):
    response = requests.get(
        url=url,
        headers=headers,
        params={"language": "en-US", "sort_by": "popularity.desc", "page": page},
        timeout=30
    )        

    return response.json()  
        

    

def main():
    url = f"{base_url}/movie/popular"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    page = 1
    max_pages = 5

    while page <= max_pages:
        try:
            with open(f'data/raw/popular_movies-{page}.json', 'w', encoding='utf-8') as f:
                json.dump(getPopularMovies(url, headers, page), f, ensure_ascii=False, sort_keys=True, indent=4)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error ocurred: {http_err}")
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not a valid JSON string.")
        except requests.exceptions.RequestException as e:
            print(f"Network/request failure on page {page}: {e}")



if __name__ == "__main__":
    main()
    
                 
            

    
    
    

    


    

    
       


        

   


  

