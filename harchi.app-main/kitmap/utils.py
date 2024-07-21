from audioop import reverse
import requests
import geonamescache
from kit365.configs import (
    MAPIR_KEY
)

MAPIR_BASE_ADDR = 'https://map.ir'
# NESHAN_KEY = os.environ['NESHAN_KEY']

cities_in_iran = []

'''
later i can write a crawler
that first reads https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86
checks the city names
then goes one link deeper and read: مختصات
https://www.amar.org.ir/%D8%A7%D8%B1%D8%AA%D8%A8%D8%A7%D8%B7-%D8%A8%D8%A7-%D9%85%D8%A7/%D8%AA%D9%82%D8%B3%DB%8C%D9%85%D8%A7%D8%AA-%DA%A9%D8%B4%D9%88%D8%B1%DB%8C
https://github.com/ahmadazizi/iran-cities/tree/master

'''

def check_persian_string(input_string):
    for ch in input_string:
        if ('\u0600' <= ch <= '\u06FF' or '\u0750' <= ch <= '\u077F' or '\u08A0' <= ch <= '\u08FF' or '\uFB50' <= ch <= '\uFDFF' or '\uFE70' <= ch <= '\uFEFF' or '\U00010E60' <= ch <= '\U00010E7F' or '\U0001EE00' <= ch <= '\U0001EEFF'):
            return True
    return False

def extract_persian_names(alternates):
    # print(alternates)
    fnames = []
    for fname in reversed(alternates):
        if check_persian_string(fname):
            fnames.append(fname)
            print(fnames)
    return list(fnames)

def feed_cities_in_iran():
    global cities_in_iran
    # Initialize the geonamescache
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities()
    cities_in_iran = [
        {
            "name": city['name'], "fnames": extract_persian_names(city['alternatenames']), 
            "longitude": city['longitude'], "latitude": city['latitude']
        } 
         for city in cities.values() if city['countrycode'] == "IR"
    ]
    return cities_in_iran


def distance_matrix(origin_lat, origin_lon, dest_lat, dest_lon, filter_mode='distance'):
    # filter_mode duration | distance
    get_distance = f'{MAPIR_BASE_ADDR}/distancematrix?origins=b,{origin_lat},{origin_lon}&destinations=c,{dest_lat},{dest_lon}&'
    'sorted=true&$filter=type eq {filter_mode}'
    headers = {
        'x-api-key': MAPIR_KEY
    }
    resp = requests.get(
        get_distance,
        headers=headers
    )
    # i have to add logger here
    if resp.status_code == 200:
        return resp.json()
    else:
        return {
            'err_msg': "something went wrong try later"
        }


def run_test():
    print("[+] testing kitmap utils")
    resp = distance_matrix(
        origin_lat='35.7219',
        origin_lon='51.3347',
        dest_lat='32.6539',
        dest_lon='51.6660',
    )
    print(resp.json())
    return resp


if __name__ == "__main__":
    run_test()