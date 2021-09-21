"""
This program takes a plain text and key input, then encrypts the 
plain text using the key.

Created on Sep 17, 2021
Author: Alex Sun
Student Number: 20289530
CISC-121
"""


def check_validity(inp):
    """Checks whether or not a non-letter char is in the 'inp' string."""
    for x in inp:
        if(x not in table):
            print("Invalid character detected. Try again.\n")
            return False
    return True;



# Alphabet repeated twice so that going above 25 in index won't 
# cause an 'out of range' error, but instead loop back to 'a' 
table="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# Loop to keep prompting user for input until valid input is achieved
while(0==0):
    text=input("Enter your plain text to be encrypted (text only please!): ")
    # For some reason, using the input function in the pydev IDE results
    # in the addition of a '\r' at the end of the input, so we have to 
    # remove that or it'll mess up our code
    # Also convert to lowercase so upper cases don't ruin the program
    text=text.replace("\r","").lower()
    if(check_validity(text)==True):
        break
while(0==0):
    key=input("Enter encryption key (any text): ")
    key=key[:-1].lower()
    if(check_validity(key)==True):
        break
output=""

# Expand key string to match or exceed the length of text for
# use in encryption
while(len(text)>len(key)):
    key+=key
    
# Encryption algorithm: A trick I noticed while looking at the
# encryption table is that if you add the indexes of the two
# input character together, you'll get the index # of the
# encrypted character (index, as in index of the alphabet)
# ex. index of b is 1, and m is 12. 1 + 12 = 13, and
# 13 in the alphabet is N.
for x in range(len(text)):
    output+=table[table.index(text[x])+table.index(key[x])]
print("\nYour encrypted text is:",output)