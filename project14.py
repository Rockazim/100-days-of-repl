from getpass import getpass as input
# ^will need to ge this from repl
#2 player rock paper scissors game. Keeps count of games won by each player and has an exit option.

print("Lets play a game of Rock Papaer Scissors!")


player1_score = 0
player2_score = 0

while True:
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
      elif player2 == "P" or player2 == "p":
        print("Player1's Rock is smothered by Player2's Paper!")
        player2_score += 1
      elif(player2 == "S" or player2 == "s"):
        print("Player1's Rock smashes Player2's Scissors!")
        player1_score += 1
      else:
        print("Try again")
    elif player1 == "P" or player1 == "p":
      if player2 == "P" or player2 == "p":
        print("You both picked Paper, draw!")
      elif player2 == "r" or player2 == "R":
        print("Player2's Rock is smothered by Player1's Paper!")
        player1_score += 1
      elif(player2 == "S" or player2 == "s"):
        print("Player2's scissors cuts Player1's paper!")
        player2_score += 1
      else:
        print("Try again")
    elif player1 == "S" or player1 == "S":
      if player2 == "S" or player2 == "S":
        print("You both picked Scissors, draw!")
      elif player2 == "P" or player2 == "p":
        print("Player1's scissors cuts Player2's Paper!")
        player1_score += 1
      elif(player2 == "R" or player2 == "R"):
        print("Player2's Rock smahes Player1's Scissors!")
        player2_score += 1
      else:
        print("Try again")
    else:
      print("Try again")
      
  elif options == 2:
    print("Scores are:\nPlayer 1:", player1_score, "\nPlayer 2:", player2_score, "\n")
  elif options == 3:
    print("Bye!")
    break
  else:
    print("Try again")