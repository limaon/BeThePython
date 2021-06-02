# PEMDASLR
# print(3 * (3 + 3) / 3 - 3)

""" 
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
 """

""" 
score = 0
height = 1.8
isWinning = True

# f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
 """

""" # ---------
age = input("Whats is your current age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
 """

""" 
print("Welcome to the tip calculator.")
tot_bill = input("What was the total bill? $")
percent = input("What percetage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

result_percent = (float(tot_bill) * (int(percent) / 100))
result_person_pay = int(result_percent + 124) / int(people)
print(f"Each person should pay: ${round(result_person_pay, 2)}")
 """

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percetage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")