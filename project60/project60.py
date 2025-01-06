"""Austomatically work out today's date.
Prompt the user to input the name and date of their event (year, month and day).
Work out the number of days until the event and output it.
If the event is happening today, insert some party emojis.
If the event was in the past, sad face emojis and tell the user how many days ago it was."""

import datetime

today = datetime.date.today()

while True:
    print("🌟Event Countdown Timer🌟")
    event_name = input("Input the event > ")
    try:
        year = int(input("Input the year > "))
        month = int(input("Input the month > "))
        day = int(input("Input the day > "))
    except:
        print("Please input a valid number!")

    event = datetime.date(year, month, day)
    
    days_till = (event - today).days
    
    if event > today:
        print(f"{event_name}\nDay: {day}\nMonth: {month}\nYear: {year}\n{days_till} days to go")
    elif event < today:
        print(f"{event_name}\nDay: {day}\nMonth: {month}\nYear: {year}\n😭😭😭😭😭 You missed it by {days_till} days!")
    else:
        print(f"{event_name}\nDay: {day}\nMonth: {month}\nYear: {year}\n🥳🥳🥳 Today!")
    
    keep_going = input("Keep going(Y/N)?").capitalize()
    if keep_going == "Y":
        continue
    else:
        break