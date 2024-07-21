import pytz
from datetime import datetime


def get_all_time_zones():
    return pytz.all_timezones


def get_timezone(timezone):
    """Get the timezone for a given country."""
    try:
        return pytz.timezone(timezone)  # Returning the first timezone for simplicity
    except KeyError:
        return None


def get_current_time(timezone):
    """Get the current time for a given country."""
    # timezone = get_timezone(country)
    if timezone:
        timezone = get_timezone(timezone)
        current_time = datetime.now(timezone)
        return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    else:
        return "Timezone not found for the given country"

timezone = "Asia/Tehran"  # Example: United States
current_time = get_current_time(timezone)
print(f"The current time in {timezone} is {current_time}")