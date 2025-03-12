import sys
import json
import pandas as pd
import requests
import base64




def findGenre(artist_name):
    """Fetches the genre of an artist from MusicBrainz API."""
    url = f"https://musicbrainz.org/ws/2/artist/?query=artist:{artist_name}&fmt=json"
    
    try:
       response = requests.get(url, headers={"User-Agent": "SpotifyPlaylistCurator/1.0 (puja.shah321@gmail.com)"})
       data = response.json()
        
        # Ensure results exi
       if "artists" in data and len(data["artists"]) > 0:
            artist = data["artists"][0]  # Take the first result
            if "genres" in artist:
                allGenres =  [genre["name"] for genre in artist["genres"]]  # Return list of genres
                return allGenres[0]
        
       return None  # No genre found
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def findGenreSpotify(artist_name):

    #setting client id for spotify:
    client_id = '92725123c83549a88b46c6200f1e6113'
    client_secret = 'a53b585c8faf4233a8b084a3a8b7b00c'

    # Encode client_id and client_secret to base64
    auth = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')

    # Send request for access token
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {auth}',
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    access_token = response.json().get('access_token')

    # Set up the headers with your access token
    headers = {
        'Authorization': f'Bearer {access_token}'}

    # Step 1: Search for the artist by name
    search_url = f'https://api.spotify.com/v1/search?q=artist:{artist_name}&type=artist&limit=1'

    response = requests.get(search_url, headers=headers)
    search_data = response.json()

    # Check if we got the artist info
    if 'artists' in search_data and search_data['artists']['items']:
        artist_id = search_data['artists']['items'][0]['id']
        artist_name = search_data['artists']['items'][0]['name']

        # Step 2: Get genres for the artist
        artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
        artist_response = requests.get(artist_url, headers=headers)
        artist_data = artist_response.json()

        genres = artist_data.get('genres', [])
        #print(f"{artist_name} : {genres}")
        if genres:
            return genres[0]
        else:
            None
    else:
        return None
    



spotify_data = sys.argv[1]


with open(spotify_data, 'r',encoding='utf-8') as file:
    data = json.load(file)

df = pd.DataFrame(data)

sample = df.head(10).copy()

sample['genre'] = sample['artistName'].apply(findGenreSpotify)
print(sample)
 
