import random
word_list = ["aardvark", "baboon", "camel"]

rando = random.choice(word_list)
print(rando)
choice = input("Guess a letter: ").lower()

if choice in rando:
    print("right")
else:
    print("wrong"
