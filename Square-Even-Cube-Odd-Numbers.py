# Kristine Joy Barrina  #BSCPE 1-5  # April 23, 2023
# Creating a python program that will create two different files then square all even numbers and cube all odd numbers.

# Pseudocode

# Open a file named integers.txt
with open ("integers.txt", "r") as integers:

# Create a variable that contains all the integers
    integer_numbers = integers.readlines()
    print (integer_numbers)
    print ("its working!")

# Initialize variables that will store even and odd integers
even_integers = []
odd_integers = []

# Use for loop with range of all integers length
for i in range (len(integer_numbers)):

# Check if integer is even 
    if (int(integer_numbers [i]) % 2) == 0:
        print ("it's even!")
        
    # Square even integer
        square_even = (int(integer_numbers [i])** 2)
        print (square_even)
        
    else:
        print ("it's odd!")

# Open a file named double.txt
# Append the squared value of even integers to double.txt
# If integer is odd, cube it
# Open a file named triple.txt
# Append the cubic value of odd integers to triple.txt
# Design the output using tkinter
