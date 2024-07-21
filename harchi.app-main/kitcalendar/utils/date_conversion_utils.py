from hijri_converter import convert
import jdatetime
from datetime import datetime


def jalali_to_gregorian(year, month, day, reverse=False):
    try:
        if reverse:
            gregorian_date = datetime(year, month, day)
            jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
            # print("Gregorian to Jalali:", jalali_date)
            return jalali_date
        else:
            jalali_date = jdatetime.date(year, month, day)
            gregorian_date = jalali_date.togregorian()
            return gregorian_date
    except Exception as e:
        print(e)
        # pass
    raise ValueError("something went wrong on date conversion")


def jalali_to_hijri(year, month, day, reverse=False):
    try:
        if reverse:
            arabic_date = (year, month, day)
            jalali_date = jdatetime.date.fromgregorian(date=convert.Hijri(*arabic_date).to_gregorian())
            return jalali_date
        else:
            jalali_date = jdatetime.date(year, month, day)
            greg = jalali_date.togregorian()
            hijri_date = convert.Gregorian(greg.year, greg.month, greg.day).to_hijri()
            return hijri_date
    except Exception as e:
        print(e)
        # pass
    raise ValueError("something went wrong on date conversion")


def gregorian_to_hijri(year, month, day, reverse=False):
    try:
        if reverse:
            arabic_date = (year, month, day)
            print(f'arabic date: {arabic_date}')
            gregorian_date = convert.Hijri(*arabic_date).to_gregorian()
            print(f'greg converted date: {gregorian_date}')
            return gregorian_date
        else:
            arabic_date = convert.Gregorian(year, month, day).to_hijri()
            return arabic_date
    except Exception as e:
        print(e)
        # pass
    raise ValueError("something went wrong on date conversion")
