import random

heads_tails = random.uniform(1, 10)
print(heads_tails)

if heads_tails < 4.99999:
    print("heads")
else:
    print("tails")

# These both do the same thing

random_h_T = random.randint(0, 1)
print(random_h_T)

if heads_tails == 0:
    print("Heads")
else:
    print("Tails")