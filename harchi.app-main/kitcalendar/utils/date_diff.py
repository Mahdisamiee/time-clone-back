
from datetime import datetime

def days_in_month(year, month):
    """Return the number of days in a given month."""
    if month == 2:  # February
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29  # Leap year
        else:
            return 28
    elif month in {4, 6, 9, 11}:  # April, June, September, November
        return 30
    else:
        return 31


def date_difference(start_date, end_date):
    """Calculate the time difference between two dates."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    years = end.year - start.year
    months = end.month - start.month
    days = end.day - start.day

    # Adjust negative months or days
    if days < 0:
        months -= 1
        days += days_in_month(start.year, start.month)
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days


