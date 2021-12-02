# L.M.A. - Louiso May Al....
# "Nothing is impossible to a determined woman."

# W.C. - Winston Churchill
# "The empires of the future will be the empires of the mind."

# R.D - Robertson Davies
# "Art lies in understanding some part of the dark forces, and
# bringing them under the control of reason"

# Sorites Paradox remove a dollar from a wealthy person, and they're still wealthy, right?
# But keep removing a dollar, and eventually they'll have $0.
# When do they cease being wealthy? Fuzzy Logic.

# Nov 29
class ListNode():
    def __init__(self, value):
        self.next = None
        self.value = value


class linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0


    def __len__(self):
        return self.counter


    def __iter__(self):
        """Initiallize iterator"""
        self.current = self.head
        return self


    def __next__(self):
        """Advance iterator to next element in list"""
        if self.current == None:
            raise StopIteration
        else:
            return_val = self.current.value
            self.current = self.current.next
            return return_val


    def append(self, x):
        new_node = ListNode(x)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.counter += 1


    def __getitem__(self, index):
        item = self.head
        for x in range(index):
            item = item.next
        return item.value


list = linked_list()
list.append(1)
list.append(2)
list.append(3)
# print(list)

for x in list:
    print(x)
