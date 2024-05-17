from random import choice, randint, shuffle
import secrets

coin = choice(["heads","tails"])
number = randint(0,100)
cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)
    
# print(coin)
# print(number)
# password = secrets.token_bytes(16)
# print(password)
