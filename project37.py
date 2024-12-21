"""This is the challenge you're looking for. This program will generate your Star Wars Name.

Ask the user to input their first & last names.
Slice the first 3 letters of the first name.
Slice the first 3 letters of the last name (surname).
Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
Finally, print them both as part of a sentence.
🥳 Extra points for getting all the inputs with just one input command and the split function."""

print("Star WARS NAME GENERATOR\n")
first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().lower()
maiden_name = input("Enter your Mum's maiden name: ").strip().capitalize()
city_name = input("Enter the city where you were born: ").strip().lower()

star_wars_name = f"Your Star Wars name is {first_name[0:3]}{last_name[0:3]} {maiden_name[0:2]}{city_name[-3:]} "
print(star_wars_name)