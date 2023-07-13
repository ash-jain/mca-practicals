"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 9 - Design the program to demonstrate difference in LocalDate, LocalDateTimestamp. Create a function which would return difference in days between two dates.
"""

from datetime import date, datetime


def days_difference(date1, date2):
    if isinstance(date1, datetime) and isinstance(date2, datetime):
        difference = abs(date2 - date1)
        return difference.seconds // 60
    elif isinstance(date1, date) and isinstance(date2, date):
        difference = abs(date2 - date1)
        return difference.days


if __name__ == "__main__":
    print('Enter your date of birth in the format dd/mm/yyyy: ', end='')
    day, month, year = map(int, input().split('/'))
    date1 = date(year, month, day)
    date2 = date.today()
    difference = days_difference(date1, date2)
    print(f"You are {difference} days old.\n")

    date2 = datetime.now()
    date1 = datetime(date2.year, date2.month, date2.day)
    difference = days_difference(date2, date1)
    print(f"{difference} minutes have passed in the day so far.")
