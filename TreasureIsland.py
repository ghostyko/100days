print("Welcome to Trasure Island.")
print("Your mission is to find the treasure")

left_right = input("You've come to a dead end. Do you want to go left or right? Choose wisely. ")
    # left continue / right fall / up or down - can't go that way
if left_right == "left":
    print("You've turned left down a road that leads to a river")

    swim_wait = input("The river is rapidly flowing. Do you want to run across the rocks or continue walking? ")
    if swim_wait == "run" or swim_wait == "run across":
        print("")
elif left_right == "right":
    print("You've fell into a sinkhole... Game Over")

