import random


num_i = 12
num_f = 5.2
num_c = 1j

num_r = [ #List / Array
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59)
]

x = num_r

"""
x = float(num_c)
"""

print("valor 1: " + str(num_r[0])) 
print("valor 2: " + str(num_r[1]))
print("valor 3: " + str(num_r[2]))
print("valor 4: " + str(num_r[3]))
print("valor 5: " + str(num_r[4]))
print("valor 6: " + str(num_r[5]))



