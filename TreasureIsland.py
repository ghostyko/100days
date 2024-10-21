print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

while True:

    left_right = input("You've come to a dead end. Do you want to go left or right? Choose wisely. ").lower() # left continue / right fall / up or down - can't go that way
    if left_right == "left":
        print("You've turned left down a road that leads to a river")

        while True:

            swim_wait = input("The river is rapidly flowing. Do you want to run across the rocks or continue walking? ").lower()
            if swim_wait == "run" or swim_wait == "run across":
                print("You've made it safely, somehow, to the other side. You can see cabins up ahead")
                # add cabin choices

                while True:

                    cabin_door = input("Which cabin do you think is the safest? Red, Yellow, or Blue").lower()
                    if cabin_door == "yellow":
                        print("You've found the Hidden Treasure!")
                        print("You've won!")
                        break
                    elif cabin_door == "red":
                        print("A witch turned around and made you melt")
                    elif cabin_door == "blue":
                        print("You fell into a vine trap")
                    break
            elif swim_wait == "continue" or swim_wait == "continue walking":
                print("You've been eaten by a wild bear... Game Over")
            else:
                print("Not a choice, choose something else")
            break
    # left or right question
    elif left_right == "right":
        print("You've fell into a sinkhole... Game Over")
    else:
        print("You can't go that way. Please choose 'left' or 'right'.")
        continue

    if cabin_door == "yellow":
        break