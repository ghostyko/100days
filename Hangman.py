import random
word_list = ["aardvark", "baboon", "camel"]

rando = random.choice(word_list)
print(rando)

placeholder = "_"
for char in rando:
    placeholder += char
    print(placeholder)

choice = input("Guess a letter: ").lower()

for letter in rando:
    if  letter == choice:
        print("right")
    else:
        print("wrong")
