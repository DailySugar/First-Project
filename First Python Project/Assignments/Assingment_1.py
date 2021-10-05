"""
This program takes a plain text and key input, then encrypts the 
plain text using the key.

Created on Sep 17, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121
"""


# Alphabet repeated twice so that going above 25 in index won't 
# cause an 'out of range' error, but instead loop back to 'a' 
table = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
text = input("Enter your plain text to be encrypted (text only please!): ")
# For some reason, my computer or keyboard produces a '\r' in 
# The end of the input string when using the input function, so 
# I'm removing it so it doesn't affect the output on my computer
# Also convert to lowercase so upper cases don't ruin the program
text = text.replace("\r","").lower()
key = input("Enter encryption key (any text): ")
key = key.replace("\r","").lower()
output = ""

for x in text:
    if x not in table:
        text = text.replace(x,"")

for x in key:
    if x not in table:
        key = key.replace(x,"")
# Expand key string to match or exceed the length of text for
# use in encryption
while len(text)>len(key):
    key += key
    
# Encryption algorithm: A trick I noticed while looking at the
# encryption table is that if you add the indexes of the two
# input character together, you'll get the index # of the
# encrypted character (index, as in index of the alphabet)
# ex. index of b is 1, and m is 12. 1 + 12 = 13, and
# 13 in the alphabet is N.
for x in range(len(text)):
    output += table[table.index(text[x]) + table.index(key[x])]
print("\nYour encrypted text is:",output)