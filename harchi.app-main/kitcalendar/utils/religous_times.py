import praytimes
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime


def get_timezone_offset(latitude, longitude):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude, lng=longitude)
    timezone = pytz.timezone(timezone_str)
    now = datetime.now()
    offset = timezone.utcoffset(now).total_seconds() / 3600
    return offset


def get_timezone(latitude, longitude):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude, lng=longitude)
    return timezone_str


def get_prayer_times(latitude, longitude, date_tuple):
    target_timezone = get_timezone(latitude, longitude)
    pt = praytimes.PrayTimes()
    # pt.setCoordinates(latitude, longitude)
    # praytimes.settings['midnight'] = "ISNA"
    timezone = pytz.timezone(target_timezone)
    timezone_offset = get_timezone_offset(latitude, longitude)
    prayer_times = pt.getTimes(date_tuple, (latitude, longitude), timezone_offset)
    # for key, value in prayer_times.items():
    #     prayer_time_utc = datetime.strptime(value, '%H:%M')
    #     prayer_time_utc = pytz.utc.localize(prayer_time_utc)
    #     prayer_time_local = prayer_time_utc.astimezone(timezone)
    #     prayer_times[key] = prayer_time_local.strftime('%H:%M')
    return prayer_times


latitude = 35.7219  # Example latitude (New York City)
longitude = 51.3347  # Example longitude (New York City)
date_tuple = (2024, 2, 24)

prayer_times = get_prayer_times(latitude, longitude, date_tuple)

# Print prayer times
print("Prayer Times for New York City on 2024-02-24:")
print("Fajr:", prayer_times['fajr'])
print("Dhuhr:", prayer_times['dhuhr'])
print("Asr:", prayer_times['asr'])
print("Maghrib:", prayer_times['maghrib'])
print("Isha:", prayer_times['isha'])