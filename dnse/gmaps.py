from django.http import HttpResponse, HttpRequest
import json
import googlemaps
import numpy as np
import re

google_maps = googlemaps.Client(key='API_KEY')

def google_lookup(lon, lat):
    temp = []
    results = google_maps.reverse_geocode((lat,lon))
    #print(results)
    for entries in results:
        for items in entries.get('address_components'):
            if bool(re.search(r'\d',items.get('long_name'))) != True and items.get('long_name') != 'United States':
                temp.append(items.get('short_name'))
            if bool(re.search(r'\d',items.get('short_name'))) != True and items.get('short_name') != 'United States':
                temp.append(items.get('short_name'))
    #print(np.unique(temp))
    return np.unique(temp)
