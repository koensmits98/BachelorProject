import numpy as np

lijst = [3,2,4,5,6]
lijst2 = [3,2,4,5,6]
lijst2.sort()

print(lijst)
indexlist = []
for i in lijst2:
    indexlist.append(lijst.index(i))
    
print(indexlist)