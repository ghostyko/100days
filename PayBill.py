import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
bill = random.choice(friends)
print(f"{bill} is paying the bill tonight")

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])
