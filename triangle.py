count = int(input('Enter the amount of numbers in the triangle:      '))
x = 1
tiv = 1
quant = 0
sum = 1
f = 0
while sum <= count:
    x = x + 1
    sum = sum + x
    quant = quant + 1
print (f'The triangle is  {quant} X {quant}')

for i in range(quant ):
    if tiv < 10:
        print( f'{tiv} ', end = '')
    else:
        print( f'{tiv}', end = '')
    for j in range(0, i ):
        
        f = f +  tiv + quant - j -1
        if f < 10:
            print(f'  {f} ', end = '')
        elif f < 100:
            print(f'   {f} '   , end = ' ')
        elif f >= 100:
            print(f'  {f} ', end = ' ')
            
        f = f - tiv
        
    f = 0
    tiv += 1
    print()
print()

# 1
# 2 6
# 3 7 10 
# 4 8 11 13
# 5 9 12 14 15


