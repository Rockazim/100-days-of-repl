#grade calculator

print("Exam Grade Calculator")
print()
exam_name = input("Name of exam: ")
print()
max_score = float(input("Max. Possible Score: "))
print()
user_score = float(input("Your score: "))
print()
percentage = round(user_score/max_score * 100, 2)

if percentage >= 90:
  print("You got", percentage, "% which is a A+")
elif percentage >= 80 and percentage < 90:
  print("You got", percentage, "% which is a A-")
elif percentage >= 70 and percentage < 70:
  print("You got", percentage, "% which is a B")
elif percentage >= 60 and percentage < 70:
  print("You got", percentage, "% which is a C")
elif percentage >= 50 and percentage < 60:
  print("You got", percentage, "% which is a D")
elif percentage >= 40 and percentage < 50:
  print("You got", percentage, "% which is a U")
else:
  print("Try again!")