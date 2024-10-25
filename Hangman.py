import random
word_list = ["aardvark", "baboon", "camel"]

rando = random.choice(word_list)
print(rando)

placeholder = ""
for char in rando:
    placeholder += "_"
print(placeholder)

choice = input("Guess a letter: ").lower()

for letter in rando:
    if  letter == choice:
        placeholder += choice
    else:
        print(placeholder)

print(placeholder)

