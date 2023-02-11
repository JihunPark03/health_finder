
import googlemaps
import pandas as pd

googlemaps_key = "AIzaSyB8_OUxxHuvSX0nDOuOFq8b6IrsiHLXkZU"
gmaps = googlemaps.Client(key=googlemaps_key)

# Load your addresses into a Pandas DataFrame
addresses = pd.read_csv(
    r'C:\Users\joonb\Desktop\python\health_finder\address.csv')

# Geocode the addresses
latitude = []
longitude = []

for index, row in addresses.iterrows():
    address = addresses['주소'].iloc[index]
    geolocation = gmaps.geocode(address)[0].get('geometry')
    lat = geolocation['location']['lat']
    lng = geolocation['location']['lng']
    latitude.append(lat)
    longitude.append(lng)


addresses['latitude'] = latitude
addresses['longitude'] = longitude

print(addresses)

addresses.to_csv('extracted_lat_lon.csv', index=False)
