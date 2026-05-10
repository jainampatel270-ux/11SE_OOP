# Learning intentions:
# - Create some default attributes of the class
# - Create the special print method that prints the status of the object

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

    
    def __str__(self):
        payment_details = 'Your pet is unregistered'
        if len(self.ccard) == 19:
            payment_details = 'Registered'

        my_status = 'Name: ' + self.name + '\n Category: ' + self.category + '\n Age: ' + str(self.age) + '\n Payment Details: ' + payment_details + '\n Vaccination Status: ' + str(self.vaccinated)
        return my_status
    
p1 = Pet('Foxy', 'Dog', 3,)
p1.ccard = '2348 2350 2082 0235'
print(p1)


#ACTIVITIES:
#1. Add a default new credit card value  of unknown

#2. In the __str__ method, let the user know if the pet has registered payment details  

#3. Add the vaccinated status  and include it in the special __str__ function