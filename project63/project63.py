"""Go back through your programs and choose some subroutines that you've used a lot. Perhaps it was your dice roller. Could be your prettyPrint. Maybe it was your 'generate random baldy insult' subroutine. Whatever. Find them.
Create a new file that contains all your best subroutines.
Import this file into your main.py and call a few to show that it work"""

import day63lib as moke
import random
import os, time

print("It's a blast from the past! Lets relive this old memory")

times = random.randint(1,10)
for i in range(times):
    moke.generate()
    time.sleep(1)
    os.system("cls")

moke.prettyprint()