# combine the cleaned datasets into final ones to use for machine learning
import pandas as pd

#load files
weather = pd.read_csv("weather-cleaned.csv", header=0, parse_dates=['datetime'])
songs_onehot = pd.read_csv("songs-cleaned-onehot-Alia.csv", header=0, parse_dates=['timestamp'])
songs_label = pd.read_csv("songs-cleaned-label-Alia.csv", header=0, parse_dates=['timestamp'])

#ensure date formatting is consistent
songs_onehot['date'] = pd.to_datetime(songs_onehot['timestamp']).dt.date
songs_onehot = songs_onehot.drop(columns='timestamp')
songs_label['date'] = pd.to_datetime(songs_label['timestamp']).dt.date
songs_label = songs_label.drop(columns='timestamp')
weather['date'] = pd.to_datetime(weather['datetime']).dt.date
weather = weather.drop(columns='datetime')

onehot_merged = pd.merge(weather, songs_onehot, on='date', how='inner')
label_merged = pd.merge(weather, songs_label, on='date', how='inner')

onehot_merged.to_csv("Alia-onehot.csv", index=False)
label_merged.to_csv("Alia-label.csv", index=False)
