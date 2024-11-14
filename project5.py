#practice using if and else statements

print("Marvel Movie Character Creator")
print("--")

spiderman = input("\nDo you like 'hanging around'?: ")
if spiderman == "Yes":
  print("Aha! You're Spider-man! Hi!")
elif spiderman == "No":
  print("Then you're not Spider-man")
  korg = input("Do you have a 'gravelly' voice?: ")
  if(korg == "Yes"):
    print("Aha! You're Korg! Hi!")
  elif korg == "No":
    print("Aww, then you're not Korg")
    marvel = input("Do you often feel 'Marvelous'?: ")
    if marvel == "Yes":
      print("Aha! You're Captain Marvel! Hi!")
    else:
      print("Looks like you aren't a Marvel character!")
else:
  print("Try Again please")
    