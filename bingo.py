'''B I N G O'''
import random


bingo_card = [
        [ 1 , 2 , 3 , 4 , 5 ],
        [ 1 , 2 , 3 , 4 , 5 ],
        [ 1 , 2 , 3 , 4 , 5 ],
        [ 1 , 2 , 3 , 4 , 5 ],
        [ 1 , 2 , 3 , 4 , 5 ]
    ]
a = 1
b = 16
bingo = 'BINGO'

# ----------------------------------------------------
for i in range(5):
    print(bingo[i], end = '   ')
            
    for j in range(5):
        card_number = random.randint(a, b)
        bingo_card[i][j] = card_number
        if card_number < 10:
            print(f'   {bingo_card[i][j]}', end = '   ')
        else:
            print(f'  {bingo_card[i][j]}', end = '   ')
    a = a + 15
    b = b + 16            
    print()
    print()
print('Press Enter to start the game\n\n')
# ----------------------------------------------------

number_list = []
for i in range(1,76):
    number_list.append(i)
is_bingo = False
count = 1    
win = [0, 0, 0, 0, 0]
while True:
    
    is_number_in = False
    create_card = input()
    
    if create_card != '':
        break
    
    else:
        
        temp = random.randint(1, len(number_list) - 1)
        number = number_list[temp]
        
        print(f'Number:    {number}\nAttempt:   {count}\n')
        
        for i in range(5):
            print(bingo[i], end = '   ')
            for j in range(5):
                
                if bingo_card[i][j] == 'X':
                    print(f'  {bingo_card[i][j]} ', end = '   ')
                else:
                    if number == bingo_card[i][j]:
                        win[i] = win[i] + 1
                        if 5 in win:
                            is_bingo = True
                            
                        is_number_in = True
                        bingo_card[i][j] = 'X'
                        print(f'  {bingo_card[i][j]} ', end = '   ')
                        
                    else:
                        if bingo_card[i][j] < 10:
                            print(f'   {bingo_card[i][j]}', end = '   ')
                        else:
                            print(f'  {bingo_card[i][j]}', end = '   ')
            print()
            print()
        number_list.remove(number)
        if is_number_in:
            print(f'{number} Marked')
        count += 1
        
        
        if is_bingo:
            print(f'\nBINGO !!!!!')
            break
        
        
        
        
                
 
    