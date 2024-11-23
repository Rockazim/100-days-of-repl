#Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. The user has to figure out the correct song lyric in as few attempts as possible. Find the true lyric master among you!




print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")

counter = 1
while True:
  print("Please don't stop the _____")
  lyric = input("")
  if lyric == "music":
    break
  else:
    print("Nope, try again.")
    counter += 1
print("Well done! It only took you", counter, "attempts.")