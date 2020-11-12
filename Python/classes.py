#First you create a class called point. Its a template for a type of object.
#a class is followed by an init method (default function/method) that defines the class.
#The first part is always going to be self variable, and followed by other inputs variables.
#self.x stores the value of first input.
#self.y stores the value of Second input.

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

#now we can call the class with its required inputs.
p = Point(2, 8)
print(p.x)
print(p.y)
#############################
#similarly we are going to write a program for flight capacity
#Declaring Class FLight first with the input argument of capacity
#Defining the Flight class along with capacity as a property.
#here we are defining an additional property called passengers and keeping it empty.
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

#Adding a new function/method called add_passenger in the class.
#we are also defining an other method to determine open seats.
#if the open_seats method returns a value than we can execute an action
#As action we are going to add the name provided as an input into the property
# using append command.

    def add_passenger(self, name):
        if not self.open_seats(): #if self.open_seats == 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

#here is how we use the class.
flight = Flight (3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"added {person} to flight successully.")
    else:
        print(f"no available seats for the person.")
