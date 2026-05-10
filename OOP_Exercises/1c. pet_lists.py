#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets
#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:
'''
Pet name: Foxy
Species: Dog
Age: 8
Vaccination Status: False
'''
#1 - Parallel List
pet_name = ['Foxy', 'Max', 'Bob']
species = ['Dog', 'Cat', 'Fish']
age = [4, 7, 2]
vaccination_status = [False, True, False]



#2 Print Parallel List
for i in range(len(pet_name)):
    print('Pet Name:', pet_name[i])
    print('Species:', species[i])
    print('Age:', age[i])
    print('Vaccination Status:', vaccination_status[i])
    print()



#3. Demonstrate what happens when an item is deleted




  #ACTIVITIES:
# In each activity test out that the printing of data is still valid
#1. Add a new animal named Hootie, its a blowfish, it is 34 years
#2. Vaccinate an unvaccinated animal (create vaccination)
#3. Remove an animal and make sure that all the printing is correct



#1. Add a new animal named Hootie, its a blowfish, it is 34 years
pet_name = ['Foxy', 'Max', 'Bob', 'Hootie']
species = ['Dog', 'Cat', 'Fish', 'Blowfish']
age = [4, 7, 2, 34]
vaccination_status = [False, True, False, False]



#2. Vaccinate an unvaccinated animal (create vaccination)
vaccination_status[2] = True



#3. Remove an animal and make sure that all the printing is correct
del pet_name[1]
del species[1]
del age[1]
del vaccination_status[1]

for i in range(len(pet_name)):
    print('Pet Name:', pet_name[i])
    print('Species:', species[i])
    print('Age:', age[i])
    print('Vaccination Status:', vaccination_status[i])
    print()