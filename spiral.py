'''Spiral'''
       
# 1  2  3  4  5  6  
# 22 23 24 25 26 7  
# 21 36 37 38 27 8  
# 20 35 42 39 28 9  
# 19 34 41 40 29 10 
# 18 33 32 31 30 11 
# 17 16 15 14 13 12

spiral = []
row = []
n = int(input('N = '))
count = 1
for i in range(int(n)):
    for j in range(int(n)):
        row.append(0)
    spiral.append(row)
    row = []

for i in range(n):
    spiral[0][i] = i + 1
down = 1
down_count = 1
down_count_n = 0
left = n
left_count = -1
left_count_n = 2
up = n
up_count = 0
right = 1
right_count = 1
right_count_n = 1

while count != n * n + +2:

    
    if down != int(n / 2)  + 2:
        for i in range(down_count,n - down_count_n):
            
            spiral[i][n - down] =spiral[i - 1][n - down] + 1    
        down_count_n += 1
        down_count +=1                                                                                        
        down +=1
        count += 1  

    if left != int(n / 2) - 1:    
        for i in range(left - 2, left_count, -1):
            spiral[left - 1][i] = spiral[left - 1][i + 1] + 1
        left_count_n +=1
        left -= 1
        left_count += 1
        count += 1  

    if up != int(n / 2) - 1:
        for i in range(up-2, up_count, -1):
            spiral[i][up_count] = spiral[i + 1][up_count] + 1
        up_count +=1
        up -= 1
        count += 1  

    if right != int(n / 2) + 1:
        for i in range(right_count, n - right_count_n):
            spiral[right_count][i] = spiral[right_count][i - 1] + 1
        right_count += 1
        right -=1
        right_count_n += 1
    
        count += 1  
for i in range(n):
    for j in range(n):
        if(spiral[i][j]) < 10:
            print(f' {spiral[i][j]}', end = '   ')
        else:
            print(f'{spiral[i][j]}', end = '   ')
        
    print()
    