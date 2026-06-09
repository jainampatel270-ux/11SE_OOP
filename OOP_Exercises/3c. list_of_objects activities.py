# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = True

    def __str__(self):
        payment_details = 'Your pet is unregistered'
        if len(self.ccard) == 16:
            payment_details = 'Registered'

        my_status = 'Name: ' + self.name + '\n Category: ' + self.category + '\n Age: ' + str(self.age) + '\n Payment Details: ' + payment_details + '\n Vaccination Status: ' + str(self.vaccinated)
        return my_status

p1 = Pet('Bonnie', 'Dog', 3, )
p2 = Pet('Om', 'Fish', 2,)
p3 = Pet('Walsh', 'Cat', 5,)
p4 = Pet('Belfort', 'Turtle', 4,)
pets = [p1, p2, p3, p4]

for Pet in pets: 
    print(Pet)
    print('')


#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list
