# 2025Spring-CMPT353-Weather-Aware Song Clustering & Classification
This project analyzes and clusters songs based on audio and genre features, then uses weather and song metadata to train a model that can classify new songs or predict song clusters in different weather contexts.

## Directories
    .
    ├── data/
    │   ├── Alia_IconAndGenre.ipynb           # Input dataset with song and weather features for Alia
    │   └── Puja_IconAndGenre.ipynb           # Input dataset with song and weather features for Puja
    ├── song-features/             
    │   ├── data/                             # Output of data cleaning
    │   │   ├── song/
    │   │   └── weather
    │   ├── data cleaning/                    # source for data cleaning files
    │   └── model/                 
    └── README.md                   

## Requirements
Install the required Python libraries with:
    <pre>pip install pandas numpy matplotlib seaborn scikit-learn hdbscan</pre>

If using a virtual environment:
    <pre>python -m venv venv
         source venv/bin/activate  # Mac/Linux
         venv\Scripts\activate     # Windows </pre>

# Data cleaning 
Step-By-Step Guide:
1. add-audio-features.py:
	role: merge personal spotify history with Kaggle dataset at https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks?resource=download to add features like energy, danceability, etc
	outputs: audio-added-Alia/Puja.csv

2. data-cleaning-songs:
	role: drop all na value + columns that aren't needed. since genre is a string and not a number, it needs to be changed. Onehot encoding is better 	for clustering and labels is better for classification, so used both (now realising that i never used this data for the classification, so it is okay to delete the label dataset lines of code + the .csvs)
	outputs: songs-cleaned-Puja/Alia.csv

3. data-cleaning-weather.py:
	role: clean data by dropping nas and unnecessary columns
	outputs: weather-cleaned.csv

4. merge-cleaned-data.py:
	role: combine all weather data + song data into (once again the label one is not needed and can be deleted)
	outputs: Merged-Puja/Alia.csv

5. clustering.py:
	role: used DBSCAN to cluster similar songs together. If some clusters were too big, use KMeans to convert those into smaller clusters (added 1000 to their id so it doesn't overlap with ids from the original DBSCAN)
	outputs: Alia/Puja-clustered.py

6. weather_audio_model.ipynb
	role: trains a Random Forest model using a Puja/Alia-clustered.csv containing cluster, and selects the top 3 recommended songs based on the current weather and recent listening trends.
	outputs: none
         
## Run Model
In the root directory run:
    <pre>jupyter-notebook</pre>
    