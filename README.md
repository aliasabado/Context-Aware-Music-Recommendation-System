# 2025Spring-CMPT353-Weather-Aware Song Clustering & Classification
This project analyzes and clusters songs based on audio and genre features, then uses weather and song metadata to train a model that can classify new songs or predict song clusters in different weather contexts.

## Directories
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
         
## Run Model
    