# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

print("Hello! World.")

print("Shreyas is a boy")
print("Shreyas is a Masters Student at University of Tuebingen")

## I dont want to use Shreyas everytime
name = "Shreyas" # string variable

print(name, "is a boy")
print(name, "is a Masters Student at University of Tuebingen")

age = 24 # integer variable
print(name, "is", age, "years old.")

height = 1.76 # float variable
print(name, "is", height, "meters tall.")

result = True # boolean variable

# Strings

Name = "Shreyas"
Name = 'Shreyas'
# print('Shreyas's height is 1.76 meters.') # This will give error
print("Shreyas's height is 1.76 meters.") # This will work
print('Shreya\'s height is 1.76 meters.') # This will also work
# is is called escaping the character


# String Concatination
Last_name = "Muragodmath"
full_name = name + " " + Last_name
print(full_name)

# String Multiplication
laugh = "ha "
print(laugh * 5)

#length of a string
print(len(full_name)) # len is a function that gives length of a string

# String Indexing and Slicing
full_name = "Shreyas Muragodmath"
# S H R E Y A S   M U R  A   G  O  D  M  A  T H
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

print(full_name[0]) # First character
print(full_name[8]) # Eighth character

# full_name[0] = 'X' # This will give error as strings are immutable
print(full_name[0]+full_name[8])

# Slicing
print(full_name[0:7]) # Slicing from index 0 to 6, 7 is excluded
print(full_name[:7]) # Slicing from index 0 to 6, 7 is excluded
print() # line break
print(full_name[8:]) # Slicing from index 8 to 


# Negative Slicing

# S   h    r   e   y   a   s      M    u  r  a  g  o  d  m   a  t   h
#-19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5  -4 -3  -2 -1
#  0  1   2   3   4   5   6   7   8    9  10 11 12 13 14 15  16 17 18

print(full_name[-1]) # last character
print(full_name[-7:]) # last 7 characters
# [start: end-1: step]
print(full_name[::-1]) # reverse the string using slicing with step -1


#00:25:00