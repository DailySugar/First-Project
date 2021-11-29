# C.L -
# "Those who seek, find."

# L.S - Louisa Strong - wrote a lot about Joseph Stalin
# "I am one of those who never knows the destination of their journey until they have arrived."

# P.A - Paul Anderson
# "Knowledge has a tricky way of turning out to be useful."

# Nov 18        Nov 22      Nov 25
# "self" is tricky
# Class attributes and functions
# Instance attributes and functions

# Abstraction - Focus on the important bits, leaving out others.
# eg. limiting pi to a few decimal places so you can compute it.

# Encapsulation - Hide information not important to end user
# - Protects the information from interference.
# - Avoids confusion if we change them

# Inheritance - Subclass inherits all attributes & functions from parents
#

# Polymorphism - Function with multiple versions for different types of objects
# eg. len([1,2,3])      len((a,b,c))        len("abcdefg")

class super_hero(object):
    # class variables
    hero_count = 0
    hero_list = []

    # class functions
    def how_many_heros():
        # returns hero count
        return super_hero.hero_count


    def list_all_heros():
        return sorted(super_hero.hero_list)


    def __init__(self, hero_name = "unknown", real_name = "unknown", image = None, powers = ["unknown"], location = "unknown"):
        self.hero_name = hero_name
        self.real_name = real_name
        self.image = image
        self.powers = powers[:]
        self.location = location
        self.allies = []
        self.enemies = []

        super_hero.hero_count += 1
        super_hero.hero_list.append(self)


    def __str__(self):
        return "It's " + self.hero_name + " from " + self.location


    def __int__(self):
        return 1337


    def __eq__(self, other):
        """Test for equality"""
        return (self.hero_name, self.real_name) == (other.hero_name, other.real_name)


    def __ne__(self, other):
        """Test for inequality"""
        return (self.hero_name, self.real_name) != (other.hero_name, other.real_name)


    def get_allies(self):
        return self.allies


# hero_1 = super_hero(hero_name = "Potato")
# hero_2 = super_hero(hero_name = "Potato")
# print(hero_1 == hero_2)
# print(int(hero_1) / 2)


class Forest():
    var_1 = 4


class Park():
    var_2 = 9


class GovProp():
    var_1 = 10


class ProvPark(GovProp, Forest, Park):
    # If there's conflicting variables, it'll pick the value from the first class listed
    pass


# pp1 = ProvPark()
# print(pp1.var_2)


# Data encapsulation: hiding information (double underscore before variable name hides it?
# Apparently doesn't work on python.
class c1():

    __counter = ()

    def get_counter():
        return c1.__counter


    def __init__(self, value):
        self.__x = value
        c1.__counter += 1


    def get_x(self):
        return self.__x


    def set_x(self, value):
        self.__x = value


thing1 = c1(5)
print(thing1.get_x())



