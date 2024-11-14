#practice with nested if, elif, and else

print("Fake Fan Finder")
print("----------------")

show = input("What's your favorite Show? ")
if show == "Prison Break":
  print("OMG REALLY?")
  prison_break_q1 = input("Who is the best character?")

  if prison_break_q1 == "Scofield":
    print("You got that by pure chance.")
    prison_break_q2 = input("Okay then, who is the worst character?")
    if prison_break_q2 == "Tbag":
      print("You are a true fan.")
    else:
      print("See Fake", show, "fan!")
  else:
    print("See Fake", show, "fan!")

elif show == "Breaking Bad":
  print("DOPE")
  breaking_bad_q1 = input("Who is the best character?")
  if breaking_bad_q1 == "Walter":
    print("You got that by pure chance.")
    breaking_bad_q2 = input("Okay then, who is the worst character?")
    if breaking_bad_q2 == "Skyler":
      print("You are a true fan.")
    else:
      print("See Fake", show, "fan!")
  else:
    print("See Fake", show, "fan!")
    
elif show == "Better Call Saul":
  print("Legend")
  better_call_saul_q1 = input("Who is the best character?")
  if better_call_saul_q1 == "Saul":
    print("You got that by pure chance.")
    better_call_saul_q2 = input("Okay then, who is the worst character?")
    if better_call_saul_q2 == "Tuco":
      print("You are a true fan.")
    else:
      print("See Fake", show, "fan!")
  else:
    print("See Fake", show, "fan!")
          
else:
  print("Try another show")
  