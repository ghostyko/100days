print("welcome to python pizza deliveries!")
size = input("size of pizza? S, M, or L: ")
# todo: work out how much they need to pay based on their size choice S:15 - M:20 - L:25
if size == "S":
    print("Price equals $15")
    bill = 15
elif size == "M":
    print("Price equals $20")
    bill = 20
elif size == "L":
    print("Price equals $25")
    bill = 25

# todo: work out how to add to their bill based on their pepperoni choice. S:+$2 - M/L: +$3
    pepperoni = input("do you want pepperoni? Y or N: ")
    if pepperoni == "Y":
        if size == "S":
            bill += 2
            print("New total is $17")
        elif size == "M":
            bill += 3
            print("New totla is $ 23")
        elif size == "L":
            bill += 3
            print("New total is $28")

# todo: work out their final amount based on whether if they want extra cheese for any size. +$1
    extra_cheese = input("do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1

    print(f"total will be {bill}")

else:
    print("Try again.")