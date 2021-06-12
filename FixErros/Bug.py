
# Describe Problem
#  def my_funtion():
    #  for i in range(1, 21):
        #  if i == 20:
            #  print("You got it")
#  my_funtion()


# Reproduce the Bug
#  from random import randint
#  dice_imgs = ['1', '2', '3', '4']
#  dice_num = randint(0, 5)
#  print(dice_imgs[dice_num])

# Play Computer
#  year = 1994
#  
#  if False:
    #  print("You are a milenial")
#  elif False:
    #  print("You are a Gen Z.")

# Print is your Friend
#  pages = 0 
#  word_per_page = 0
#  pages = int(input("Number of pages: "))
#  word_per_page == int(input("Number of words per page: "))
#  total_words = pages * word_per_page
#  print(f"pages = {pages}")
#  print(f"word_per_page = {word_per_page}")
#  print(total_words)

#  def mutate(a_list):
    #  b_list = []
    #  for item in a_list:
        #  new_item = item * 2
        #  b_list.append(new_item)
    #  print(b_list)
#  
#  mutate([1, 2, 3, 5, 8, 13])


for number in range(1, 101):
    print(f"Currently on number {number}")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)

