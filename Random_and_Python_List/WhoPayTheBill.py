import random

# Split string method
names_string = input("Gives me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

# Write your code below this line 
# Get the total number of items in list
num_itens = len(names)

random_choice = random_name = random.randint(0, num_itens - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")