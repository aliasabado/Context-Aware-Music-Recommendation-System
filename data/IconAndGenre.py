import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
music_data = pd.read_csv("song_genres_mapped_Alia.csv")  # Replace with actual filename
weather_data = pd.read_csv("vancouverWeather.csv")  # Replace with actual filename

# Convert timestamps to datetime format
music_data['timestamp'] = pd.to_datetime(music_data['endTime'])
weather_data['timestamp'] = pd.to_datetime(weather_data['datetime'])

# Round timestamps to nearest hour for merging
music_data['timestamp'] = music_data['timestamp'].dt.round('H')
weather_data['timestamp'] = weather_data['timestamp'].dt.round('H')

# Merge Data on Timestamp
merged_data = pd.merge(music_data, weather_data, on='timestamp', how='inner')

# Scatter Plot: Genre vs Temperature
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='icon', y='genre', hue='icon', alpha=0.7)
plt.title("Music Genre vs Temperature by Weather Condition")
plt.xlabel("Temperature (°C)")
plt.ylabel("Music Genre")
plt.legend(title="Weather Condition")
plt.show()

# Histogram: Genre Distribution by Weather Condition
plt.figure(figsize=(12, 6))
sns.countplot(data=merged_data, x='genre', hue='weather_icon')
plt.title("Music Genre Distribution by Weather Condition")
plt.xticks(rotation=90)
plt.xlabel("Music Genre")
plt.ylabel("Count")
plt.legend(title="Weather Condition")
plt.show()

# Box Plot: Temperature by Genre (Separated by Weather Condition)
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_data, x='genre', y='icon', hue='weather_icon')
plt.xticks(rotation=90)
plt.title("Temperature Distribution by Genre and Weather Condition")
plt.xlabel("Music Genre")
plt.ylabel("Temperature (°C)")
plt.legend(title="Weather Condition")
plt.show()