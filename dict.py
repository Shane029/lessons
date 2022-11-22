import random

mydict = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0   
}

for _ in range(1000):
    x = random.randint(2, 12)
    if x in mydict:
        mydict[x] += 1
for i in mydict:
    mydict[i] = mydict[i] / 10
    print(f'{i} -- {mydict[i]}')
    
print(sorted(mydict, key = mydict.get))
