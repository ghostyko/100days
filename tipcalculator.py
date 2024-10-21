print("Welcome to the tip calculator!")
total_bill_inp = float(input("What was the total bill? $")) #Can be a float bc bills include decimals
tip_give = int(input("How much tip would you like to give? 10 12 15 "))
split = int(input("How many people to split the bill? "))

bill_with_tip = ((tip_give / 100) * total_bill_inp + total_bill_inp)
each_pay = round((bill_with_tip / split), 2)
print(f"Each person should pay: ${each_pay}")