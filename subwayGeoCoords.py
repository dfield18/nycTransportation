import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import time
import pandas as pd
        
# list of all subway station
path = 'C:/Users/David/Documents/subway_ridership.csv'

# create dataframe with subway stations
df = pd.read_csv(path, encoding = "ISO-8859-1")
stations =  df['Station (alphabetical by borough)']

url = 'https://maps.googleapis.com/maps/api/geocode/json'
count = 0

# loop through each dataframe row to find geo-coordinates of subway stations
# code to find longitude and latitude adapted from stackoverflow.com/questions/37311687/extracting-lat-lon-from-geocode-result-list-with-python-google-maps-api
 
for x in range(0, 422):
    station = stations[x]
    station = station.replace("\xa0", " ")
    params = {'sensor': 'false', 'address': station, 'city': 'New York City'}
        r = requests.get(url, params=params)       
    results = r.json()['results']
    location = results[0]['geometry']['location']   
    lat = location['lat']
    lon = location['lng']
    # each row contains latitude, longitude and station name
    print(lat, " ", lon, " ", station)
    count = count +1
    time.sleep(1)
    