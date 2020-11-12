#Here we are showing how to try and catch exceptions.

#sys module helps detect system errors and lets us take action
import sys

#try to get input if the input results in a value error display msg and exit 1.
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

#Try to divide x/y but if a ZeroDivisionError appears catch and display msg.
#and exit with error code 1
try:
    result = x / y

except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
