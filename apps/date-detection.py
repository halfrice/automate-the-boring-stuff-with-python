import re

dateRegex = re.compile(
    r'(\d{2})/(\d{2})/(\d{4})',
    re.VERBOSE,
)

calendar = {
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


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False


def validateDate(date):
    # mo stands for match object (from the book)
    mo = dateRegex.search(date)
    if mo:
        month = int(mo.group(1))
        day = int(mo.group(2))
        year = int(mo.group(3))
    else:
        return False

    # Validate months
    if month not in calendar:
        return False

    # Validate days
    i = 1 if month == 2 and isLeapYear(year) else 0
    if day < 1 or day > (calendar[month] + i):
        return False

    # Validate years
    if year < 1000 or year >= 3000:
        return False

    return True


date = input('Input a date in MM/DD/YYYY format: ')
isValidDate = validateDate(date)
if isValidDate:
    print(f'{date} is valid')
else:
    print(f'{date} is not valid')
