#Here we have a dictionary array
people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slither"}
]

#this will tell the sort function to sort by name.
#def f(person):
#    return person["name"]

#people.sort(key=f)
#instead of defining it separately we can define it in one line using lambda
# lambda functionname: functionname ["output parameter"]
people.sort(key=lambda person: person["name"])
print(people)
