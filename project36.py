"""Create a list of people's names. Ask for first and last name (surname) separately.
Strip any extra spaces.
Store names in a capitalized version.
Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
Add those new versions to a list.
Do not allow duplicates.
Each time you add a new name, you should print out the full list.
"""

names = []

while True:
    first_name = input("First Name: ").strip().capitalize()
    last_name = input("Last Name: ").strip().capitalize()

    full_name = f'{first_name} {last_name}'

    if full_name not in names:
        names.append(full_name)
        print()
        for x in names:
            print(x)
        print()
    else:
        print("\nERROR: Duplicate name")
        print(f"\n{full_name}\n")