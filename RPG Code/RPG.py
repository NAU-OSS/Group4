import random


# Dice Roller Class used the ranint function to determine the total amount
# based on the number of sides of the dice.
class DiceRoller:
    def roll(self, times, sides):
        total = 0
        for i in range(times):
            roll = random.randint(1, sides)
            total += roll
        return total

r = DiceRoller()


class Attack:
    # initializes a new attack object.
    def __init__(self, name, number_of_dice, sides_of_die, damage_type):
        self._name = name
        self._sides = sides_of_die
        self._number = number_of_dice
        self._type = damage_type

    # returns the type of attack
    def get_attack_type(self):
        return self._type

    # returns damage sustained by character by calling the DiceRoller class
    def get_damage(self):
        damage = r.roll(self._number, self._sides)
        return damage

    # Returns the name of character
    def get_name(self):
        return self._name

    # Allows user to change the name of the character
    def set_name(self, new_name):
        self._name = new_name

    # getters and setters for the side of dice
    def get_sides(self):
        return self._sides

    def set_sides(self, new_sides):
        self._sides = new_sides

    # getters and setters for the number of dice
    def get_number(self):
        return self._number

    def set_number(self, new_number):
        self._number = new_number

    # the string return of the class. Returns name of attack based on
    # physical or magic
    def __str__(self):
        if self._type == "physical":
            return "Slash"
        elif self._type == "magic":
            return "Fireball"


class Adventurer:
    # initializes a new adventurer
    def __init__(self, name, hit_points, armor, magic_resistance, initiative):
        self._name = name
        self._hit_points = hit_points
        self._armor = armor
        self._magic_resistance = magic_resistance
        self._initiative = initiative

    # getters and setters for the name that return or change name
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # getters and setters for the armor points return or change armor
    def get_armor(self):
        return self._armor

    def set_armor(self, new_armor):
        self._armor = new_armor

    # getters and setters for magic resistance points return or change magic
    # resistance
    def get_magic_resistance(self):
        return self._magic_resistance

    def set_magic_resistance(self, new_magic_rsistance):
        self._magic_resistance = new_magic_rsistance

    # getters and setters for hit points returns or changes hit points value
    def get_hit_points(self):
        return self._hit_points

    def set_hit_points(self, new_hit_points):
        self._hit_points = new_hit_points

    # getters and setters for initiative returning or changing the value
    def get_initiative(self):
        return self._initiative

    def set_initiative(self, new_initiative):
        self._initiative = new_initiative

    # checks if the character is alive based on the the hit points value
    def is_alive(self):
        if self._hit_points > 0:
            return True
        else:
            return False

    # assigns a roll initiative randomly based on the initiative of the object
    def roll_initiative(self):
        number = random.randint(0, self._initiative)
        return number

    # Calculates the damage sustatined by a character based on the
    # damage type and amount
    def take_damage(self, amount, damage_type):
        # calculates the damage based on a phyical type attack and
        # armor of defender
        if damage_type == "physical":
            if self._armor >= int(amount):
                print("%s resists all damage!" % self._name)
            else:
                reduced_damage = amount - self._armor
                self._hit_points -= reduced_damage
                if self._hit_points > 0:
                    print(self._name + " suffers " + str(reduced_damage) +
                          " damage after " + str(self._armor) +
                          " armor and has " + str(self._hit_points) +
                          " hit points left.")
                else:
                    print("\n%s has won with %i hit points left!" %
                          (a.get_name().capitalize(), a.get_hit_points()))
        # calculates damage to character based on magic attack and magic
        # resistance of defender
        elif damage_type == "magic":
            if self._magic_resistance >= int(amount):
                print("%s resists all damage!" % self._name)
            else:
                reduced_damage = amount - self._magic_resistance
                self._hit_points -= reduced_damage
                if self._hit_points > 0:
                    print(self._name + " suffers " + str(reduced_damage) +
                          " damage after " + str(self._magic_resistance) +
                          " magic resistance and has " +
                          str(self._hit_points) + " hit points left.")
                else:
                    print("\n%s has won with %i hit points left!" %
                          (b.get_name().capitalize(), b.get_hit_points()))


# Creates Fighters class inherits from Adventurer Class
class Fighter(Adventurer):
    # class member variables for a Fighter
    _HP = 40
    _ARMOR = 10
    _MR = 4

    # Initialization for new Fighter object
    def __init__(self, name, initiative):
        super().__init__(name, Fighter._HP, Fighter._ARMOR,
                         Fighter._MR, initiative)
        self._melee = Attack("Slash", 1, 8, "physical")

    # returns attack of Fighter
    def get_attack(self):
        return self._melee

    # assigns the damage number and type of Fighter, stores info in a
    # tuple, and returns tuple
    def strike(self):
        damage = int(Attack.get_damage(self._melee))
        type = Attack.get_attack_type(self._melee)
        info = (damage, type)
        # prints info about the character, damage, and type
        print(self._name + " attacks with " + str(self._melee) + " for " +
              str(damage) + " physical damage")
        return info

    # returns a string with the stats of the Fighter
    def __str__(self):
        return self._name + " with " + str(self._HP) + "\
 hit points and a " + str(self._melee) + " attack."


# creates wizard character class inherits from Adventurer Class
class Wizard(Adventurer):
    # class members variables
    _HP = 20
    _ARMOR = 4
    _MR = 10

    # initializes a new Wizard object
    def __init__(self, name, initiative):
        super().__init__(name, Wizard._HP, Wizard._ARMOR,
                         Wizard._MR, initiative)
        self._melee = Attack("Fireball", 3, 6, "magic")

    # returns attack for wizard
    def get_attack(self):
        return self._melee

    # assigns the damage number and type of Fighter, stores info in a
    # tuple, and returns tuple
    def cast(self):
        damage = int(Attack.get_damage(self._melee))
        type = Attack.get_attack_type(self._melee)
        info = (damage, type)
        # prints name of character, damage, and type
        print(self._name + " attacks with " + str(self._melee) + " for " +
              str(damage) + " magic damage")
        return info

    # returns a string with the stats of the Wizard
    def __str__(self):
        return self._name + " with " + str(self._HP) +\
               " hit points and a " + str(self._melee) + " spell."

# calls the classes and creates battle
if __name__ == "__main__":
    print("")
    print("-----------------------------------------------------------")
    # creates Fighter
    a = Fighter("Aragorn", 20)
    print("Created: ", a)
    # creates Wizard
    b = Wizard("Gandalf", 20)
    print("Created: ", b)
    print("-----------------------------------------------------------")
    round = 1
    # checks if both characters are still alive and continues battle if
    # condition is met
    while a.is_alive() and b.is_alive():
        print("")
        print("** Round %i **" % round)
        round += 1
        x = a.roll_initiative()
        y = b.roll_initiative()
        # determines who goes first based on roll initiative and prints
        # who won and the damage suffered by defender.
        if x > y:
            print("%s wins initiative!" % a.get_name())
            damage = b.take_damage(a.strike()[0], "physical")
        else:
            print("%s wins initiative!" % b.get_name())
            damage = a.take_damage(b.cast()[0], "magic")
