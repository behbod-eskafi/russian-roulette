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

game = int(input("WHICH GAME WOULD YOU LIKE TO PLAY?\n 1.Classic Game\n 2.Advanced Game\nplease enter the number: "))
if game == 1:
 classic_game(number_of_players,bullet)
else:
  pass
