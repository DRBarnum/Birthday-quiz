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

if todaymonth == 9:
    a="September"
elif todaymonth == 10:
    a="October"
elif todaymonth == 11:
    a="November"
elif todaymonth == 12:
    a="December"
elif todaymonth == 1:
    a="January"
elif todaymonth == 2:
    a="February"
elif todaymonth == 3:
    a="March"
elif todaymonth == 4:
    a="April"
elif todaymonth == 5:
    a="May"
elif todaymonth == 6:
    a="June"
elif todaymonth == 7:
    a="July"
elif todaymonth == 8:
    a="August"


name= (input("Hello, what is your name? "))
month= (input("Hi " + name + ", what was the name of the month you were born in? "))
year= int(input("And what year were you born in, " + name + "? "))
day= int(input("And the day? "))
if month== "October" and day== 31:
    print("You were born on Halloween!")
elif day== todaydate and month== a:
    print("Happy birthday!")
elif month in("September", "October", "November", "9", "10", "11"):
    if year >=1980 and year <=1989:
        print(name + ", you are a fall baby of the eighties.")
    if year < 1980:
        print(name + ", you are a fall baby of the Stone Age.")
    if year >= 1990 and year <= 1999:
        print(name + ", you are a fall baby of the nineties.")
    if year >= 2000:
        print(name + ", you are a fall baby of the two thousands.")
elif month in("December", "January", "February", "12", "1", "2"):
    if year >=1980 and year <=1989:
        print(name + ", you are a winter baby of the eighties.")
    if year < 1980:
        print(name + ", you are a winter baby of the Stone Age.")
    if year >= 1990 and year <= 1999:
        print(name + ", you are a winter baby of the nineties.")
    if year >= 2000:
        print(name + ", you are a winter baby of the two thousands.")
        
elif month in("March", "April", "3", "4"):
    if year >=1980 and year <=1989:
        print(name + ", you are a spring baby of the eighties.")
    if year < 1980:
        print(name + ", you are a spring baby of the Stone Age.")
    if year >= 1990 and year <= 1999:
        print(name + ", you are a spring baby of the nineties.")
    if year >= 2000:
        print(name + ", you are a spring baby of the two thousands.")
else:
    if year >=1980 and year <=1989:
        print(name + ", you are a summer baby of the eighties.")
    if year < 1980:
        print(name + ", you are a summer baby of the Stone Age.")
    if year >= 1990 and year <= 1999:
        print(name + ", you are a summer baby of the nineties.")
    if year >= 2000:
        print(name + ", you are a summer baby of the two thousands.")

        