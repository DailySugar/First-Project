'''
Created on Sep 18, 2021

@author: alexs
'''

import pydoc

def test(listlists,target):
    if type(listlists) is not list:
        return None
    else:
        count=0
        for l in listlists:
            if type(l) is not list:
                return None
            else:
                if target in l:
                    count+=1
        return count            
print(test([[1,0],[2,3,4],[0,6,7,1,1,3],["w","n",1]],1))