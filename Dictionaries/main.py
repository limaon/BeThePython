programming_dictionary = {
    "Bug": "An error in program that prevents the program",
}

# Retrieving items from dictionary.
#print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something"

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an exstiong dictionary
#programming_dictionary = {}

# Edit an iten in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])