#this is how you define a function. and input can be mentioned in parenthesis.
def square(x):
    return x * x
# the following will loop through 1-9  and output the square of that number.
#we can also import a function from a different file, see square.py for details/
#from functions import square
for i in range(10):
    print(f"the square if {i} is {square(i)}")
