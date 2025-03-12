import json
import pandas as pd

### Step 1: Load Data Files ###
music_data_file = "StreamingHistory_music_Puja.json"  # Your Spotify JSON file
genre_map_file = "genre_map.json"  # Separate genre map file

# Load the JSON music data
with open(music_data_file, "r", encoding="utf-8") as file:
    song_data = json.load(file)

# Load the JSON genre map
with open(genre_map_file, "r", encoding="utf-8") as file:
    genre_map = json.load(file)

# Convert JSON data to DataFramev
df = pd.DataFrame(song_data)

### Step 2: Assign Genres Based on Artist Name ###
df["genre"] = df["artistName"].map(genre_map)

# Fill missing genres with "Unknown"
df["genre"].fillna("Unknown", inplace=True)

### Step 3: Save the Updated Data ###
output_file = "song_genres_mapped.csv"
df.to_csv(output_file, index=False)
print(f"\nFile saved as {output_file}")

# Display final results
print("\nFinal Results with Mapped Genres:")
print(df[["artistName", "trackName", "genre"]].head(20))
