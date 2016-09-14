"""
birthday.py
Author: Robbie
Credit: Matt
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

print(todaymonth,"/", todaydate,"/ 2016")
name= (input("What is your name?"))
month= (input("What month were you born in?"))
if month in("September", "October", "November"):
    print("You are a fall baby")
elif month == [12, 1, 2]:
        print("You are a winter baby")
elif month == [3, 4]:
    print("You are a spring baby")
else:
    print("You are a summer baby")
        