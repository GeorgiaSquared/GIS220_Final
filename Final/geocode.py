import geocoder
import pandas as pd

# Obtained from https://www.bingmapsportal.com
BING_API_KEY = ""


# Bing API free tier doesn't allow for bulk processing over 50? entries
# Easier to query for each individual location. We just need the latlng from the geocoder object.
def get_coords(place):
    return geocoder.bing(place, key=BING_API_KEY).latlng


# read the CSV into a Pandas 'DataFrame'. Latin-1 encoding was needed for the source file
df = pd.read_csv("geocode/MidWestEmoChart.csv", encoding='latin-1')

# map function applies the "getCoords" function to every value in the "CityStateCountry" column. 
# The resulting coordinates are then appended to a new "Coordinates" column in the DataFrame.
df["Coordinates"] = df["CityStateCountry"].map(getCoords)  

df.to_csv("MidWestCoords.csv")
