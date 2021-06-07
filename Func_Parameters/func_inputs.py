# Simple Function

"""
def greet():
    print("hello")
    print("How do you do?")
    print("Isn't the wheather nice today?")

greet()
"""

# Function that alows for input
"""
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Alvaro")  
"""

#  Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What ist like in {location}")

#  greet_with("Alvaro", "Manaus")


# Function with keyword arguments
greet_with(location="London", name="Angela")
