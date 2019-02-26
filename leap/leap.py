import datetime

def is_leap_year(year=datetime.datetime.now().year):
    if isinstance(year, int):
        if year%4 == 0 and (year%100 != 0 or year%400 == 0):
            return True
        return False
    raise TypeError("Input should be an integer e.g. 1999 or 2012")
