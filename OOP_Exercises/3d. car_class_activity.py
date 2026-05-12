# Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year,drivetrain=None,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.drivetrain = drivetrain
        self.price = price
        self.for_sale = False
      

    def __str__(self):
        if self.for_sale == True:
            print('c1 is for sale')
        car_stats = '\n Make: ' + str(self.make) + '\n Model: ' + str(self.model) + '\n Year: ' + str(self.year) + '\n Drivetrain: ' + str(self.drivetrain) + '\n Price: ' + str(self.price) + '\n For Sale: ' + str(self.for_sale)
        return car_stats



c1 = Car('Mazda','Neo',2005, 'FWD', 23000)

c2 = Car('Lexus', 'CXV', 2020, 'AWD', 45000)
c2.for_sale = 'For sale'

c3 = Car('Mercedes', 'S Class', 2025, 'AWD', 67000)
c3.for_sale = 'For sale'

cars = [c1, c2, c3]

for car in cars:
    print(car)


#ACTIVITIES:
#1. Istantiate another car object
#2. Add another attribute (for_sale)
#3. Add sale status for sale or not for sale to the __str__ method
#4. Create 2 more cars and print all car statuses with a loop