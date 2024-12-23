"""Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
Finally, output the whole dictionary (keys and values).
🥳 Extra points for getting all the inputs with just one input command and the split function."""


print("🌟Website Rating🌟")

website = {"name" : None, "url" : None, "description" : None, "rating" : None}
q1 = input("\nInput the website name: ")
q2 = input("Input the URL: ")
q3 = input("Input your a description: ")
q4 = input("Input the a star rating out of 5: \n")
print()
website['name'],website['url'],website['description'],website['rating'] = q1, q2, q3, q4

for x, values in website.items():
    print(f'{x}: {values}')