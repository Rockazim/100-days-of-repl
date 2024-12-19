"""Let's extend this program and build option 4: "Get SPAMMING".

Print out the first 10 email addresses with a custom email sent to each of those people.
Print one email at a time, pause, and then clear the screen before the next email is printed."""

import time,os
listOfEmail = []
import random

def prettyPrint():
    os.system("clear") 
    print("listofEmail") 
    print()
    for index in range(len(listOfEmail)): # len counts how many items in a list
        print(f"{index}: {listOfEmail[index]}") 
        time.sleep(1)

def emailbomb():
    os.system("clear")
    counter = 1
    for location in range(len(listOfEmail)):
        message = random.randint(0,9)
       
        print(f"Email {location}\n")
        print(f"Dear {listOfEmail[location]}")

        if message == 0:
            print("It has come to our attention that you've yet to join the Ultimate Cat Yoga Challenge. We highly recommend you start immediately. Failure to do so will result in us sending your email to every cat meme creator on Earth and signing you up for the 'Pawsome Life of Garfield' daily digest. You’ll also be legally obligated to start saying 'purr-fect' in every conversation.")
            
            time.sleep(3)
            print("\nWhiskers and meows,")
            time.sleep(1)
            print("Sir Fluffington IV")
        
        
        
        elif message == 1:
            print("We noticed you haven’t tried our revolutionary 'Pineapple Pizza Appreciation' course. If you don't enroll by tomorrow, we’ll forward your email to fruit purists worldwide and register you for the 'Anchovy Lovers Monthly.' Just imagine the judgment.")
            time.sleep(3)
            
            print("\nSlices and spices,")
            time.sleep(1)
            print("Tony Crustopherson")


        elif message == 2:
            print("It seems you haven’t downloaded the 'Bird Calls for Beginners' app yet. If you continue to neglect this life-changing opportunity, we’ll have no choice but to enroll you in the 'Duck Quacks Daily' mailing list and gift you a lifetime subscription to 'Seagulls Screaming at Dawn FM.'")
            time.sleep(3)
            print("\nTweet tweet,")
            time.sleep(1)
            print("Bea Chirpson")



        elif message == 3:
            print("We noticed you’re ignoring the '101 Uses for Leftover Pasta Water' seminar. If this continues, we’ll leak your email to an underground group of gluten-free conspiracy theorists and ensure you receive hourly updates on spaghetti lore.")
            time.sleep(3)
           
            print("\nA-peelingly,")
            time.sleep(1)
            print("Professor Split McSmoothie")


        elif message == 4:
            print("You’ve skipped out on joining the 'Sock Puppetry for Adults' workshop. If you don’t sign up immediately, we’ll send your contact info to 'Mismatched Socks Anonymous' and gift you 12 years’ worth of newsletters on the history of argyle.")
            time.sleep(3)
            print("\nWarm regards,")
            time.sleep(1)
            print("Knittie McSockface")




        elif message == 5:
            print("We saw you haven’t enrolled in the 'Intro to Underwater Basket Weaving' masterclass. Should you persist in this neglect, we’ll add you to the 'Seaweed Enthusiasts Network' and also ensure you’re looped into 'Shark Facts Hourly.'")
            time.sleep(3)
            print("\nPieced together,")
            time.sleep(1)
            print("Ed Cornerstonington")


        elif message == 6:
            print("You’ve missed your chance to sign up for the 'Extreme Llama Grooming' retreat. If you don’t register by the end of the day, we’ll subscribe you to 'Alpaca Life Weekly' and send your email to a llama sanctuary with questionable data privacy practices.")
            time.sleep(3)
            print("\nFluffily yours,")
            time.sleep(1)
            print("Dr. Lana Alpaca")


        elif message == 7:
            print("We noticed you haven’t joined the 'Squirrel Whispering 101' online course. If you don’t take action immediately, we’ll ensure your inbox is flooded with 'Acorn Hoarders Quarterly' and sign you up for 'Nut Facts Daily.' Your new nickname will also be 'Squeaky McSquirrelface.'")
            time.sleep(3)
            print("\nChittering regards,")
            time.sleep(1)
            print("Professor Acorn von Nutty")


        elif message == 8:

            print("It’s clear you’re avoiding the 'Potato Stamp Art for Beginners' workshop. If you don’t sign up soon, we’ll add you to the 'Tater Enthusiasts Newsletter' and send your email to an underground group of radical sweet potato activists. Your inbox may never recover.")
            time.sleep(3)
            print("\nMashed and smashed,")
            time.sleep(1)
            print("Spudly McStarchington")

        elif message == 9:    

            print("It seems you’ve neglected to participate in the 'Ultimate Paperclip Origami Championship.' If this oversight continues, we’ll enroll you in the 'Stationery Hoarders Anonymous' mailing list and forward your email to binder clip manufacturers worldwide. Expect unsolicited catalogs.")
            time.sleep(3)
            print("\nFolded fondly,")
            time.sleep(1)
            print("Clip von Paperhold")



        if counter == 10:
            break
        else:
            time.sleep(1)
            os.system("clear")
        counter += 1

while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu =="2":
        email = input ("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint() 
    elif menu == "4":
        emailbomb()
    time.sleep(1)
    os.system("clear")