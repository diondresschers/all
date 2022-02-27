# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print("# \"\"\" direct onder de functie is een docstring, en maakt duidelijk wat die functie doet. Sluit ook af met \"\"\"")
def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month, that year."""

    if not 1 <= month <= 12:
        return "Deze maand bestaat niet"

    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

dagen = days_in_month(2000,6)

print(dagen)





