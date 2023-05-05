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

    # To get absolute value when t2 greater than t1
    if t2 > t1:
        # Function calculates a timedelta, which only supports seconds and milliseconds
        seconds = abs((t2 - t1).seconds) 
    else:
        seconds = abs((t1 - t2).seconds)

    hours = seconds / 3600 # A minute is 60 seconds, an hour is 60 minutes
    return hours

def dateTimeDiff(start, end):    
    """Returns difference between two moments

    Args:
        v1 (str): time value in format YYYY-mm-dd hh:mm:ss
        v2 (str): time value in format YYYY-mm-dd hh:mm:ss

    Returns:
        float: difference in hours
    """
    v1 = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    v2 = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    difference = abs(v2 - v1)
    seconds = difference.total_seconds()
    hours = seconds / 3600
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
    value = round(difference / divider)
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

def dateTimeDiff2(start, end, unit):
    """Calculates difference between date time values

    Args:
        start str: time value in format YYYY-mm-dd hh:mm:ss
        end str: time value in format YYYY-mm-dd hh:mm:ss
        unit str: name of the unit: day, hour, minute, second

    Returns:
        _type_: _description_
    """
    v1 = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    v2 = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    difference = abs(v2 - v1)
    units = {'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}
    divider = units[unit]    
    seconds = difference.total_seconds()
    value = seconds / divider
    return value

def sortWeekdays(weekday):
    weekdayNumber = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 
     'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    try:
        value = f'{weekday} is the week\'s {weekdayNumber[weekday]}. day'
    except Exception as e:
        value = f'{weekday} is not a weekday, check your input'
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

    print(dateTimeDiff('2023-04-28 10:00:00', '2023-04-29 11:00:00')), 'tuntia'