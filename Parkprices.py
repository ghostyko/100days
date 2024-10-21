print("Welcome to the park!")

height = int(input("what is your height? "))

if height >= 120:
    print("you can ride!")
    age = int(input("how old are you? "))
    if age <= 12:
        bill = 5
        print("Kids $5")
    elif age <= 18:
        bill = 7
        print("Youth $7")
    elif age <= 64:
        bill = 12
        print("Adults 12")
    elif age >= 45 and age <= 55:
        bill = 10
        print("Crisis $10")
    elif age >= 65:  # anything 65 or more - NOT 64
        bill = 9
        print("Senior $9")

    photo = input("Do you want a picture? Type y for yes and n for No")
    if photo == "y":
        # add $3 to their bill
        bill += 3
else:
    print("Sorry, you're not tall enough")