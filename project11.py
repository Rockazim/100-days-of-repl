#calculates How many seconds are in a year and accounts for leap year(extra day)

leap_year = input("Would you like to check if a year is a leap year? (y/n)")
if leap_year == "y":
  print("Ok here you go!", 60*60*24*366)
else:
  print("Ok here you go!", 60*60*24*365)