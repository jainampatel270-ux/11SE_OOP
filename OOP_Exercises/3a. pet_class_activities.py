# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class Pet:
    def __init__(self, name, category, age, vaccination_status, ccard, billing_a, owner_name, account ):
        self.name = name
        self.category = category
        self.age = age
        self.vaccination_status = vaccination_status
        self.ccard = 'Unknown'
        self.billing_a = 'Unknown'
        self.owner_name = 'Unknown' 
        self.account = 0

p1 = Pet('Bonnie', 'Cat', 3, 'Vaccinated', '1234 5678 9823 1234', 'Colobee Ave , 6741', 'Jeff', 0)
print(p1.name)
print(p1.category)
print(p1.age)
print(p1.vaccination_status)
print(p1. ccard)
print(p1.billing_a)
print(p1.owner_name)
print(p1.account)

p2 = Pet('Foxy', 'Dog', 5, 'Not Vaccinated', '1234 5678 9823 1234', 'Colobee Ave , 6741', 'Jeff', 0)
print(p2.name)
print(p2.category)
print(p2.age)
print(p2.vaccination_status)
print(p2. ccard)
print(p2.billing_a)
print(p2.owner_name)
print(p2.account)


#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)