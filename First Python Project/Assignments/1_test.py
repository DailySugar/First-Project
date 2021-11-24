dict1 = {1:[[1,2,3],{1,2,3}],2:2,3:3}
dict2 = dict1.copy()
dict2[1][0] = dict1[1][0].copy()

dict1[1][0].append("ayo")

print(dict2,dict1)