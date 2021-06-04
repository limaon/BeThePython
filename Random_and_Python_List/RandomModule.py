import random

""" 
random_interger = random.randint(1, 10)
print(random_interger)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
 """

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
