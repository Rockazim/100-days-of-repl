#focusing on elif

print("MY LOGIN SYSTEM")
print("+++++++++++++++")
username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "password":
  print("Why hello there", username, "what a lovely accent you have, you could have charmed your way in even without a password")
elif username == "anna" and password == "anamist":
   print("heyooo", username, "hope you're doing well!")
  
elif username == "zimmy" and password == "zimmyjr.":
  print("Whats up", username, "didn't know you were here")

else:
  print("Try again")