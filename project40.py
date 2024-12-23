"""Today's challenge is to create a contact card using a dictionary.

Ask the user to input their name, date of birth, telephone number, email and physical address.
Store it all in a dictionary.
Print it out in a nice way once its stored."""


print("🌟Contact Card🌟\n")
question1 = input("Input your name > \n").capitalize()
question2 = input("Input your date of birth > \n")
question3 = input("Input your telephone number > \n")
question4 = input("Input your email > \n")
question5 = input("Input your address > \n")
print("\n------------------\n")

myUser = {"name": question1, "dob": question2, "telephone": question3, "email" : question4, "address":question5}
print(f"Name: {myUser['name']}")
print(f"DOB: {myUser['dob']}")
print(f"Tel: {myUser['telephone']}")
print(f"Email: {myUser['email']}")
print(f"Address: {myUser['address']}")


print(f"\nHi {myUser['name']}. Our dictionary says that you were born on {myUser['dob']}, we can call you on {myUser['telephone']}, email {myUser['email']}, or write to {myUser['address']}.")