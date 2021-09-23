text,key,output="abc","zyx",""
table="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
for x in range(len(text)):
    output+=table[table.index(text[x])+table.index(key[x])]
print("\nYour encrypted text is:",output)