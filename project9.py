#project dealing with casting

year = int(input("What year were you born?"))
if(year >= 1925 and year <= 1946):
  print("You're a traditionalist!")
elif(year >= 1947 and year <= 1964):
  print("You're a baby boomer!")
elif(year>= 1965 and year <= 1981):
  print("You're a gen x!")
elif(year>= 1982 and year <= 1995):
  print("You're a millenial!")
elif(year>= 1996 and year <= 2015):
  print("You're a gen z!")
else:
  print("Try again!")