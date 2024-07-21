import requests
from bs4 import BeautifulSoup
from jdatetime import date as jdate
from datetime import datetime
from kitcalendar.utils.date_conversion_utils import (
    jalali_to_gregorian,
    jalali_to_hijri,
    gregorian_to_hijri
)

dn_dict = {
    'saturday': {
        'gregorian': "saturday",
        'jalali': "شنبه",
        'hijri': "شنبه",
    },
    'sunday': {
        'gregorian': "sunday",
        'jalali': "یکشنبه",
        'hijri': "یکشنبه",
    },
    'monday': {
        'gregorian': "monday",
        'jalali': "دوشنبه",
        'hijri': "دوشنبه",
    },
    'tuesday': {
        'gregorian': "tuesday",
        'jalali': "سه شنبه",
        'hijri': "سه شنبه",
    },
    'wednesday': {
        'gregorian': "wednesday",
        'jalali': "چهارشنبه",
        'hijri': "چهارشنبه",
    },
    'thursday': {
        "gregorian": "thursday",
        "jalali": "پنج شنبه",
        "hijri": "پنج شنبه",
    },
    'friday': {
        'gregorian': "friday",
        'jalali': "جمعه",
        'hijri': "جمعه",
    },
}

jalali_monthes = [
    'فروردین', 'ادریبهشت', 'خرداد',
    'تیر', 'مرداد', 'شهریور',
    'مهر', 'آبان', 'آذر',
    'دی', 'بهمن', 'اسفند',
]

hijri_monthes = [
    'محرم', 'صفر', 'ربیع الاول',
    'ربیع الثانی', 'جمادی الاول', 'جمادی الثانی',
    'رجب', 'شعبان', 'رمضان',
    'شوال', 'ذیقعده', 'ذیحجه',
]


def get_day_and_month_name(year, month, day, date_type):
    global dn_dict, jalali_monthes, hijri_monthes
    if date_type == "gregorian":
        # we need jalali and hijri data
        jd = jalali_to_gregorian(year, month, day, True)
        hd = gregorian_to_hijri(year, month, day)
        dayn_res = dn_dict[
            datetime(year, month, day).strftime("%A").lower()
        ]
        print(f"month is {jd.month}")
        day_res = {
            'jalali': jd.day,
            'hijri': hd.day
        }
        month_res = {
            'jalali': jalali_monthes[jd.month-1],
            'hijri': hijri_monthes[hd.month-1]
        }
        year_res = {
            'jalali': jd.year,
            'hijri': hd.year,
        }
    elif date_type == "jalali":
        # we need gregorian and hijri data
        gd = jalali_to_gregorian(year, month, day)
        hd = jalali_to_hijri(year, month, day)
        dayn_res = dn_dict[gd.strftime("%A").lower()]
        day_res = {
            'hijri': hd.day,
            'gregorian': gd.day
        }
        month_res = {
            'hijri': hijri_monthes[hd.month-1],
            'gregorian': gd.strftime("%B").lower()
        }
        year_res = {
            'hijri': hd.year,
            'gregorian': gd.year
        }
    else:
        # we need jalali and gregorian data
        gd = gregorian_to_hijri(year, month, day,True)
        jd = jalali_to_hijri(year, month, day,True)
        dayn_res = dn_dict[gd.strftime("%A").lower()]
        day_res = {
            'jalali': jd.day,
            'gregorian': gd.day
        }
        month_res = {
            'jalali': jalali_monthes[jd.month-1],
            'gregorian': gd.strftime("%B").lower()
        }
        year_res = {
            'jalali': jd.year,
            'gregorian': gd.year
        }

    return year_res, month_res, day_res, dayn_res


def jalali_month_days(year, month):
    try:
        isleap = True
        jdate(year, 12, 30)
    except ValueError:
        isleap = False
    normal_month_days = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30 if isleap else 29]
    return normal_month_days[month-1]


def get_calendar(year, month):
    try:
        jalali_date = jdate(year, month, 1)
    except Exception as e:
        return str(e)
    
    # Calculate the number of days in the specified month
    jalali_days = jalali_month_days(year, month)
    
    # Create a list of dictionaries representing each day in the month
    days_in_month = []
    for day in range(1, jalali_days + 1):
        gregorian_date = jalali_date.togregorian()
        # hijri_date = convert_to_hijri(jalali_date)
        day_name = jalali_date.strftime('%A')  # Get Jalali day name
        days_in_month.append({
            'jalali': f"{year}-{month:02d}-{day:02d}",
            'gregorian': gregorian_date.strftime('%Y-%m-%d'),
            'jalali_day_name': day_name,
            'day_of_week': jalali_date.weekday() + 1  # Get the day of the week (1-7)
            # 'hijri': hijri_date
        })
        try:
            jalali_date = jalali_date.replace(day=day + 1)
        except:
            pass
    return days_in_month


print(get_calendar(1402, 12))

def get_events_of_month(year, month):
    resp = requests.post('https://www.time.ir/', data={'year': 1403, 'month': 1})
    b = BeautifulSoup(resp.content)
    # str(b.find_all('div', {'id': "ctl00_cphTop_Sampa_Web_View_EventUI_EventCalendarSimple30cphTop_3732_ecEventCalendar_pnlMainCalendar"})[0])
    # b.find_all('eventsCurrentMonthWrapper')
    # b.find_all('class=eventsCurrentMonthWrapper')
    # b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})
    # b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})[1]
    # b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})[0]
    # b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})[0].find_all('li', {'class': 'eventHoliday'})
    # b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})[0].find_all('li', {'class': ''})
    # returns date
    # int(b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})[0].find_all('li', {'class': 'eventHoliday'})[0].find('span').text[0:2])

    results = b.find_all('div', {'class': 'eventsCurrentMonthWrapper'})[0].find_all('li', {'class': 'eventHoliday'})
    res = [re.text for re in results]
    fres = [re.split('\r\n') for re in res]
    final_results = []
    for item in fres:
        ni = []
        for i in item:
            if i.strip() != "":
                ni.append(i.strip())
        final_results.append(ni)
    return final_results
