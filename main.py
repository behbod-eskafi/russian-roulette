#Russian Roulette
import random

players = int(input("Number of players: "))
#print(person)
bullet = random.randint(1, players)
# print(bullet)

person = 0
while True:
  if bullet == person:
    print(f"Player number {person}: you lost!")
    break
  if person > 0:
    print(f"Player {person} is safe!")
  person = int(input("Your number: "))
  continue
