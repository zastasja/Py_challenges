def is_year_leap(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if is_year_leap(year) == True and month == 2:
        return 29
    elif is_year_leap(year) == False and month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31


def day_of_year(year, month, day):
    if day <= days_in_month(year, month):
        count = 0
        if month > 1:
            for i in range(1, month):
                count += days_in_month(year, i)
            return count+day
        else:
            count = day
            return count
    else:
        return None

assert day_of_year(2000, 1, 20) == 20
assert day_of_year(1900, 3, 3) == 62
assert day_of_year(2016, 2, 29) == 60