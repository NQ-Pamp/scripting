from math import *

character_name = "pamp"
character_age = 29


def say_hi(name):
    if name == "Pamp":
        print("Hello " + name + " !")
    else:
        print("Hello stranger !")


say_hi("Pamp")
print(character_name + " is " + str(character_age))

my_num = 8

# print func
print(str(my_num))
print(max(5, 9))
print(pow(4, 9))
print(round(3.3))
print(ceil(3.1))

# list
warriors = ["Tiny", "Axe", "Tusk"]

# Dico
our_numbers = {
    8: "Malik",
    16: "Pamp",
}
print(our_numbers.get(8, "No valid key found"))

# While game
word = "Pamp"
guess = ""
count = 0
no_guesses = False

while guess != word and not no_guesses:
    if count < 5:
        guess = input("Enter guess : ")
        count += 1
    else:
        no_guesses = True
if no_guesses:
    print('You lost, out of guesses :(')
else:
    print("Word found !")

# For loops
for index in range(8):
    print(index)
