# C.L -
# "Those who seek, find."

# L.S - Louisa Strong - wrote alot about Joseph Stalin
# "I am one of those who never knows the destination of their journey until they have arrived."

# Nov 18    Nov 22
# "self" is tricky
# Class attributes and functions
# Instance attributes and functions

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


    def get_allies(self):
        return self.allies


# hero_1 = super_hero(hero_name = "Potato")
# print(hero_1)
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


pp1 = ProvPark()
print(pp1.var_2)