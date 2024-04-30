import random

number_of_players = int(input("Number of players: "))

bullet = random.randint(1, number_of_players)
# print(bullet)

def classic_game(number_of_players, bullet):
  print("\n-------------------------------------------------------------------")
  print("Here are the rules for a classic game of russian roulett:\n 1. You have to take turns on inserting the number.\n 2. You have to put the numbers in mathematical order not randomly.\nHave fun, hope you don\'t die!")
  print("-------------------------------------------------------------------\n")
  person = 0
  while True:
    if bullet == person:
      print(f"***Player with number {person} just died!***")
      break
    if person > 0:
      print(f"*Player with number {person} is safe!*")
    person = int(input("Your number: "))
    continue

def advanced_game(number_of_players, bullet):
  print("\n---------------------------------------------------------------------------------------")
  print("Here are the rules for a more advanced game of russian roulett:\n 1. You insert the names of players\n 2. The turns are chosen randomly, \n    when it\'s your turn be careful to choose a number that hasn\'t been chosen by others\n    (NO CHEATING)\nHave fun, hope you don\'t die!")
  print("---------------------------------------------------------------------------------------\n")
  players_names = []
  for p in range(number_of_players):
    name = input(f"Player {p+1}\'s name: ")
    players_names.append(name)

  players_and_choices = {}
  change_player = True
  while number_of_players != 0:
    # print(players_names)
    if change_player == True:
      turn = random.randint(0,number_of_players-1)
    else:
      turn = players_names.index(player)
    player = players_names[turn]
    choice = int(input(f"\nIt\'s {player}\'s turn to choose a number: "))
    if choice not in players_and_choices.values():
      players_and_choices[player] = choice
      if choice == bullet:
        print(f"\n***{player} just died.***")
        break
      print(f"\n*{player} is safe.*")
      number_of_players -= 1 
      players_names.remove(player)
      change_player = True
    else:
      print('\n**Invalid.**')
      print(f"It was {list(players_and_choices.keys())[list(players_and_choices.values()).index(choice)]}\'s choosen number.\nTRY AGAIN.\n")
      change_player = False

game = int(input("WHICH GAME WOULD YOU LIKE TO PLAY?\n 1.Classic Game\n 2.Advanced Game\nplease enter the number: "))
if game == 1:
 classic_game(number_of_players,bullet)
else:
  advanced_game(number_of_players, bullet)
