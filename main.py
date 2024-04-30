#Russian Roulette
import random

players = int(input("Number of players: "))
#print(person)
bullet = random.randint(1, players)
# print(bullet)

person = 0
while True:
  if bullet == person:
    print(f"Palyer number {person}: you lost!")
    break
  person = int(input("Your number: "))
  continue
