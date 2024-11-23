from getpass import getpass as input
"""Go find your Rock, Paper, Scissors game from Day 14 and add the code here before you start. We are going to build upon this game.

Use a loop to repeat the game multiple rounds.
Keep score of player 1 and player 2.
End the game when a player wins three rounds using break and exit.
Use continue to restart the round until one player wins three rounds.
Your last bit of code should be the results of which player won.
"""

print("Lets play a game of Rock Papaer Scissors!")


player1_score = 0
player2_score = 0

while True:

  if player1_score == 3 or player2_score == 3:
    if player1_score ==3:
      print("Player 1 wins!")
      print("Thanks for playing!")
      exit()
    else:
      print("Player 2 wins!")
      print("Thanks for playing!")
      exit()
      
  options = int(input("Type 1 to play:\n"
    "Type 2 to see scores:\n"
    "Type 3 to exit:\n"))

  
  if options == 1:
    print("Select your move (R, P or S)")
    player1 = input("Player 1 > ")
    player2 = input("Player 2 > ")

    if player1 == "R" or player1 == "r":
      if player2 == "R" or player2 == "r":
        print("You both picked Rock, draw!")
        continue
      elif player2 == "P" or player2 == "p":
        print("Player1's Rock is smothered by Player2's Paper!")
        player2_score += 1
        continue
      elif(player2 == "S" or player2 == "s"):
        print("Player1's Rock smashes Player2's Scissors!")
        player1_score += 1
        continue
      else:
        print("Try again")
        continue
    elif player1 == "P" or player1 == "p":
      if player2 == "P" or player2 == "p":
        print("You both picked Paper, draw!")
        continue
      elif player2 == "r" or player2 == "R":
        print("Player2's Rock is smothered by Player1's Paper!")
        player1_score += 1
        continue
      elif(player2 == "S" or player2 == "s"):
        print("Player2's scissors cuts Player1's paper!")
        player2_score += 1
        continue
      else:
        print("Try again")
        continue
    elif player1 == "S" or player1 == "S":
      if player2 == "S" or player2 == "S":
        print("You both picked Scissors, draw!")
        continue
      elif player2 == "P" or player2 == "p":
        print("Player1's scissors cuts Player2's Paper!")
        player1_score += 1
        continue
      elif(player2 == "R" or player2 == "R"):
        print("Player2's Rock smahes Player1's Scissors!")
        player2_score += 1
        continue
      else:
        print("Try again")
        continue
    else:
      print("Try again")
      continue
  elif options == 2:
    print("Scores are:\nPlayer 1:", player1_score, "\nPlayer 2:", player2_score, "\n")
  elif options == 3:
    print("Bye!")
    break
  else:
    print("Try again")