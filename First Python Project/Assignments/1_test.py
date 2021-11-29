from copy import deepcopy


dict1 = {1:[[1,2,3],{1,2,3}],2:2,3:3}
dict2 = deepcopy(dict1)

dict1[1][1] = 420

print(dict2)