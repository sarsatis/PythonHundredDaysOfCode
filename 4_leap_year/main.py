def is_leap(input_year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(input_year, input_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(input_year) and input_month == 2:
        return 29
    return month_days[input_month - 1]


# Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
