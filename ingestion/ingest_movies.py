import os
import requests
from dotenv import load_dotenv
import json
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError


load_dotenv()

access_token = os.getenv('TMDB_READ_ACCESS_TOKEN')
api_key = os.getenv('TMDB_API_KEY')
base_url = "https://api.themoviedb.org/3"


def getPopularMovies(url, headers, page):
    response = requests.get(
        url=url,
        headers=headers,
        params={"language": "en-US", "sort_by": "popularity.desc", "page": page},
        timeout=30
    )        

    return response.json()  

def validate_movie_data(page, schema):
    filename = f"popular_movies-{page}.json"

    try:

        with open(f"data/raw/{filename}", "r", encoding="utf-8") as file:
            data = json.load(file)

        validate(instance=data, schema=schema)

        
        print(f"{filename} passed validation")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found.")
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid/broken JSON syntax.")
    except ValidationError as e:
        print(f"Validation failed in '{filename}' at path {list(e.path)}:\n")
        print(f"Reason: {e.message}")
    except SchemaError as e:
        print(f"Your validation schema rules are broken: {e.message}")

    return False


        

    

def main():

    movie_schema = {
       "title": "MovieListResponse",
       "type": "object",
       "required": ["page", "results"],
       "properties": {
           "page": {"type": "integer", "minimum": 1},
           "results": {
               "type": "array",
               "items": {
                   "type": "object",
                   "required": [
                        "adult", "backdrop_path", "genre_ids", "id", 
                        "original_language", "original_title", "overview", 
                        "popularity", "poster_path", "release_date", 
                        "softcore", "title", "video", "vote_average", "vote_count"
                    ],
                    "properties": {
                        "adult": {"type":"boolean"},
                        "backdrop_path": {"type": ["string", "null"]},
                        "genre_ids": {"type": "array", "items": {"type": "integer"}},
                        "id": {"type": "integer"},
                        "original_language": {"type": "string"},
                        "original_title": {"type": "string"},
                        "overview": {"type": "string"},
                        "popularity": {"type": "number"},
                        "poster_path": {"type": "string"},
                        "release_date": {"type": "string", "format": "date"},
                        "softcore": {"type": "boolean"},
                        "title": {"type": "string"},
                        "video": {"type": "boolean"},
                        "vote_average": {"type": "number"},
                        "vote_count": {"type": "integer"}
                    }
               }
           }
       }
    }
    url = f"{base_url}/movie/popular"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    page = 1
    max_pages = 5

    while page <= max_pages:
        try:
            data = getPopularMovies(url, headers, page)
            with open(f'data/raw/popular_movies-{page}.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
            validate_movie_data(page, movie_schema)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error ocurred: {http_err}")
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not a valid JSON string.")
        except requests.exceptions.RequestException as e:
            print(f"Network/request failure on page {page}: {e}")

        page += 1



if __name__ == "__main__":
    main()
    
                 
            

    
    
    

    


    

    
       


        

   


  

