import random
word_list = ["aardvark", "baboon", "camel"]

rando = random.choice(word_list)


placeholder = ""
for char in rando:
    placeholder += "_"
print(placeholder)

correct_letters = []

game_over = False
while not game_over:
    choice = input("Guess a letter: ").lower()

    display = ""

    for letter in rando:
        if letter == choice:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")