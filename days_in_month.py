# Scenario
# Your task is to write and test a function which takes two arguments (a year and a month) 
# and returns the number of days for the given month/year pair 
# (while only February is sensitive to the year value, your function should be universal).

def is_year_leap(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if is_year_leap(year)== True and month == 2:
        return 29
    elif is_year_leap(year)== False and month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31
        
# tests data

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
