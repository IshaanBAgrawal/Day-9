# using dictionaries
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}
# print(programming_dictionary)
# print(programming_dictionary["Bug"])

# adding an item in a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# emptying a dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# looping through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
