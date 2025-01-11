import os
"""Build a login system for two types of user.

Your program should:

Have two types of user - admin and normal. Each should have their own username and password.
The admin user should be greeted with 'Hello admin'.
The normal user should be greeted with 'Hello normie'."""
print("🌟 Login System 🌟")

while True:
  username = input("\nUsername > ").lower()
  password = input("\nPassword > ").lower()
  if password == os.environ['adminpw'] and username == os.environ['adminusername']:
      print("\nHello Admin!")
      break
  elif password == os.environ['normalpw'] and username == os.environ['normalusername']:
      print("\nHello normie!")
      break
  else:
      print("\nDoesn't exist!")
