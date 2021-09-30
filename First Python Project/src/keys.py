animals = {"Hudston":"dog","Mocha":"cat","Gus":"sloth"}

print(animals)
print(len(animals))

'''for pet in animals:
    print(pet,"is a", animals[pet])
print(type(animals))'''

str = {"abc":"awooo"}
del str["abc"]
#print(str)
'''
for k,v in iter(animals.items()):
    print(v)
    print(k)
'''

set = {1,2,3,4,5,6}
set.add(5)
set.update([7,8])

print(set)


thing = [("hourse",12),("dug",90),("i",1),("tr",15)]
thing.sort(key = lambda x:x[1], reverse=True)
print(thing)

x = lambda thing:thing[1]
print(x)