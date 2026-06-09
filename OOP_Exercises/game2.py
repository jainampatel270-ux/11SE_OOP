import random


# BASE CLASS
class Fighter:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_dead(self):
        return self.health <= 0

    def basic_attack(self):
        return random.randint(self.attack // 2, self.attack * 2)

    def take_damage(self, damage):
        damage = damage - self.defense
        if damage > 0:
            self.health -= damage
            print(self.name, "takes", damage, "damage")
        else:
            print(self.name, "blocks the attack")


# PLAYER CLASS
class NullCaste(Fighter):

    def adaptive_mimicry(self):
        print("Adaptive Mimicry Attempted")

        energy = random.randint(50, 100)
        strain = random.randint(10, 40)

        print("Energy =", energy, "Strain =", strain)

        if energy - strain > 40:
            print("Adaptive Mimicry Successful")
            self.defense -= 2
            return self.basic_attack() * 2
        else:
            print("Adaptive Mimicry Failed")
            return self.basic_attack()


# ENEMY CLASS
class Enemy(Fighter):

    def basic_attack(self):
        return super().basic_attack()


class Agather(Fighter):

    def ability(self):
        print("Overclock Injection Activated")

        if random.randint(1, 100) > 55:
            self.attack += 10
            self.defense -= 5
            print("Agather stats boosted")

        return self.basic_attack()


#story starts here
print("Eryndor, a nation divided by genetic castes")
print("Rules are enforced by the Agathers")
print("You are Null Caste. You were not meant to survive\n")

player = NullCaste("Null Caste", 100, 20, 5)

print("You awaken during experimentation")
print("Alarm Activated")
print("White-Coat Guard Approaching\n")


# CHAPTER 1
enemy1 = Enemy("White-Coat Guard", 80, 15, 5)

while not player.is_dead() and not enemy1.is_dead():

    print(player.name, "HP:", player.health)
    print(enemy1.name, "HP:", enemy1.health)

    print("\n1 Attack")
    print("2 Ability")
    choice = input("> ")

    if choice == "1":
        dmg = player.basic_attack()
    else:
        dmg = player.adaptive_mimicry()

    enemy1.take_damage(dmg)

    if enemy1.is_dead():
        print("White-Coat Guard DEFEATED")
        break

    print("\nEnemy attacks...")
    player.take_damage(enemy1.basic_attack())


# CHAPTER 2
print("\nYou return to your district")
print("You meet survivors and join The Off-Grids")

print("1 Brute Caste Training")
print("2 Phantom Caste Training")
choice = input("> ")

if choice == "1":
    print("You are now training with the Brute Caste")
    print("Iron Skin unlocked → Damage reduction ability gained")
else:
    print("You are now training with the Phantom Caste")
    print("Shadow Strike unlocked → High damage critical attack gained")

player.attack += 3


# CHAPTER 3
print("\nAgather surveillance tower detected")
print("1 Sabotage Tower")
print("2 Leave")
choice = input("> ")

if choice == "1":
    print("The tower has been destroyed")
    print("Reward: +10 Health gained from system disruption")
    player.health += 10
else:
    print("Mission Abandoned")


# CHAPTER 4
enemy2 = Enemy("Hunter Caste", 100, 20, 8)

while not player.is_dead() and not enemy2.is_dead():

    print(player.name, "HP:", player.health)
    print(enemy2.name, "HP:", enemy2.health)

    print("\n1 Attack")
    print("2 Ability")
    choice = input("> ")

    if choice == "1":
        dmg = player.basic_attack()
    else:
        dmg = player.adaptive_mimicry()

    enemy2.take_damage(dmg)

    if enemy2.is_dead():
        print("Hunter Caste DEFEATED")
        break

    print("\nEnemy attacks...")
    player.take_damage(enemy2.basic_attack())

# FINAL BOSS
print("\nThe Agather Caste Appears")

boss = Agather("AGATHER", 150, 30, 15)

while not player.is_dead() and not boss.is_dead():

    print(player.name, "HP:", player.health)
    print(boss.name, "HP:", boss.health)

    print("\n1 Attack")
    print("2 Ability")
    choice = input("> ")

    if choice == "1":
        dmg = player.basic_attack()
    else:
        dmg = player.adaptive_mimicry()

    boss.take_damage(dmg)

    if boss.is_dead():
        print("AGATHER DEFEATED")
        break

    print("\nBoss attacks...")
    player.take_damage(boss.basic_attack())

    if random.randint(1, 100) > 60:
        print("Overclock Injection Activated")
        boss.attack += 10
        boss.defense -= 5

print("\nTHE END OF ERYNDOR")