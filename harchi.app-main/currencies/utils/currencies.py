from bs4 import BeautifulSoup
import requests
from jdatetime import datetime
from kitcalendar.utils.current_time import get_current_time


def get_multilingual_currencies(data):
    english_translations = {
        'بورس': 'Stock Exchange',
        'انس طلا': 'Gold Ounce',
        'مثقال طلا': 'Gold Mesghal',
        'طلا ۱۸': '18 Carat Gold',
        'سکه': 'Coin',
        'دلار': 'Dollar',
        'یورو': 'Euro',
        'نفت برنت': 'Brent Crude Oil',
        'بیت کوین': 'Bitcoin'
    }
    for entry in data:
        entry['eitem'] = english_translations.get(entry['item'], 'Translation Not Found')

    return data


def get_currencies_online():
    r = requests.get("https://www.tgju.org/profile/price_dollar_rl/charts")
    b = BeautifulSoup(r.content)
    elem = b.find("div", {'class': "footer-quickview mobile-hide"})
    my_list = []
    for item in elem.find_all('li'):
        try:
            flag = item.attrs['class'][0].strip()
            res = '+' if flag == 'high' else '-'
        except:
            res = ''
            flag = ''
        i = item.find('strong').text
        j = item.find('span').find_all('span')
        print(j)
        my_list.append({'item': i, 'price': j[0].text, 'rate': res+j[1].text, 'flag': flag})
    # date = b.find('div', {'class': 'date'}).find('span').text
    timezone = "Asia/Tehran"  # Example: United States
    current_time = get_current_time(timezone)
    return {
        'currencies': get_multilingual_currencies(my_list), 
        'date': str(datetime.now().date()),
        'time': str(current_time).split()[1]
    }

'''
import pickle


get_currencies_online()
import redis
conn = redis.Redis('localhost')
resp = get_currencies_online()
resp
import datetime
now = datetime.datetime.now()
for item in resp:
    key = item['item']
    price = item['price']
    conn.hmset(key, {'price': price, 'last_time': str(now)})

for item in resp:
    key = item['item']
    it = conn.hgetall(key)
    print(it['price'])


for item in resp:
    key = item['item']
    price = item['price']
    p_dict = pickle.dumps({'price': price, 'last_time': str(now)})
    conn.set(key, p_dict)
for item in resp:
    key = item['item']
    it = pickle.loads(conn.get(key))
    print(it['price'])

(datetime.datetime.now() - now).seconds > 5*60
conn.set('currency_prices', pickle.dumps({'list': resp, 'time': now}))
conn.loads(conn.get('currency_prices'))
pickle.loads(conn.get('currency_prices'))

'''