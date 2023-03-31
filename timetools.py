# TOOLS FOR DATE AND TIME CALCULATIONS
# ====================================

# LIBRARIES AND MODULES
import datetime # Python's internal date-time library

def datediff(d1, d2):
    """Calculates the difference between two time values

    Args:
        d1 (str): time value in format yy-mm-dd
        d2 (str): time value in format yy-mm-dd

    Returns:
        float: time difference in years
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    return difference

def timediff(t1, t2):
    """Calculates the difference between two time values

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    seconds = abs((t2 - t1).seconds) # Function calculates a timedelta, which only supports seconds and milliseconds
    hours = seconds / 3600 # A minute is 60 seconds, an hour is 60 minutes
    return hours

def datediff2(d1, d2, unit):
    """Returns the difference between two dates in chosen unit (day, month or year)

    Args:
        d1 (str): 1st date in ISO format (YYYY-mm-dd)
        d2 (str): 2nd date in ISO format (YYYY-mm-dd)
        unit (str): unit to return

    Returns:
        float: difference between dates in desired units
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days) # Timedelta in days (abs makes sure there'll never be a negative number as answer)
    units = {'day': 1, 'year': 365, 'month': 30} # Dictionary for unit dividers
    divider = units[unit] # Choose by unit argument
    value = difference / divider
    return value

def timediff2(t1, t2, unit):
    """Calculates the difference between two time values in chosen unit (hour, minute, second)

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss
        unit (str): unit to return

    Returns:
        float: time difference in chosen units
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    units = {'hour': 3600, 'minute': 60, 'second': 1}
    seconds = abs((t2 - t1).seconds) # Function calculates a timedelta, wh1ich only supports seconds and milliseconds
    divider = units[unit] # Choose divider according to unit argument
    value = seconds / divider
    return value

if __name__ == "__main__":

    # Let's test date difference
    date1 = '2023-03-21'
    date2 = '2023-03-17'

    ero = datediff2(date1, date2, 'day')
    print('Ero oli', ero, 'päivää')

    # Let's test time difference
    time1 = '10:00:00'
    time2 = '15:25:00'

    ero = timediff2(time1, time2, 'minute')
    print('Ero oli', ero, 'minuuttia')