print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

while True:
    left_right = input("You've come to a dead end. Do you want to go left or right? Choose wisely. ").lower()

    if left_right == "left":
        print("You've turned left down a road that leads to a river.")

        while True:
            swim_wait = input(
                "The river is rapidly flowing. Do you want to run across the rocks or continue walking? ").lower()
            if swim_wait in ["run", "run across"]:
                print("You've made it safely, somehow, to the other side. You can see cabins up ahead.")

                while True:
                    cabin_door = input("Which cabin do you think is the safest? Red, Yellow, or Blue? ").lower()
                    if cabin_door == "red":
                        print("You found a treasure in the red cabin! You win!")
                        exit()
                    elif cabin_door == "yellow":
                        print("You've been trapped in a yellow cabin... Game Over")
                        break  # Exit the cabin loop
                    elif cabin_door == "blue":
                        print("The blue cabin is empty... Game Over")
                        break  # Exit the cabin loop
                    else:
                        print("Not a choice, choose Red, Yellow, or Blue.")

                break  # Exit the swim_wait loop after cabin choices

            elif swim_wait in ["continue", "continue walking"]:
                print("You've been eaten by a wild bear... Game Over")
                break  # Exit the swim_wait loop to restart the game
            else:
                print("Not a choice, choose something else.")
                continue
    elif left_right == "right":
        print("You've fallen into a sinkhole... Game Over")
    else:
        print("You can't go that way. Please choose 'left' or 'right'.")
        continue
print("Thank you for playing!")