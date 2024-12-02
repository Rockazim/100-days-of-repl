import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    stopMusic = int(input("Press 2 if you would like to stop the music. "))
    if stopMusic == 2:
      pause()
      return
    else:
      continue

while True:
  # clear the screen 

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input
  os.system("clear")
  time.sleep(1)
  print("🎵 MyPOD Music Player")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit\n")
  time.sleep(1)
  print("Press anything else to see the menu again")
  option1 = int(input(""))
  
  if option1 == 1:
    print("Lets have some fun!")
    play()
  elif option1 == 2:
    print("Bye!")
    exit()
  else:
    continue