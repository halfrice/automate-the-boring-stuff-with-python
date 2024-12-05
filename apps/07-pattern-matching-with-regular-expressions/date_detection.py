#!/usr/bin/env python3

# date_detection.py

import re

date_regex = re.compile(
    r'(\d{2})/(\d{2})/(\d{4})',
    re.VERBOSE,
)

CALENDAR = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    # elif year % 4 == 0 and year % 100 != 0:
    #     return True
    return False


def validate_date(date):
    mo = date_regex.search(date)  # mo stands for match object (from the book)
    if mo:
        month = int(mo.group(1))
        day = int(mo.group(2))
        year = int(mo.group(3))
    else:
        return False

    # Validate months
    if month not in CALENDAR:
        return False

    # Validate days
    i = 1 if month == 2 and is_leap_year(year) else 0
    if day < 1 or day > (CALENDAR[month] + i):
        return False

    # Validate years
    if year < 1000 or year >= 3000:
        return False

    return True


date = input('Input a date in MM/DD/YYYY format: ')
is_valid_date = validate_date(date)
if is_valid_date:
    print(f'{date} is valid')
else:
    print(f'{date} is not valid')
