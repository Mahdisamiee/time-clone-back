import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# api/prayertimes/" # at last part we have to add city id
# https://prayer.aviny.com/GIS/TimeZone.ashx?Lat=31.466446551252865&Lon=48.21418007393257
# AVINY_LOCATION_BASE = "https://prayer.aviny.com/GIS/TimeZone.ashx"
# /api/prayertimes/5

# base address
AVINY_BASE_ADDR = "https://prayer.aviny.com/"
# Aviny city codes
AVINY_CITY_LIST_ADDR = "https://prayer.aviny.com/api/city"


def get_city_pray_table(city_code):
    resp = requests.get(AVINY_BASE_ADDR + f'City_Time.aspx?Code={city_code}')
    b = BeautifulSoup(resp.content)
    tables = b.find_all('table')
    
    dfs = pd.read_html(str(tables[1]))
    temp = list(json.loads(dfs[0].to_json()).values())
    print(temp)
    return json.dumps(temp)


# TODO: write all of these based on lat lon

def get_city_time_info(city_code):
    resp = requests.get(AVINY_BASE_ADDR + f'api/prayertimes/{city_code}')
    return resp.json() # returns a dict


def get_city_list():
    resp = requests.get(AVINY_CITY_LIST_ADDR)
    return resp.json() # it returns a list


def run_test():
    print("[+] testing kitcalendar utils")
