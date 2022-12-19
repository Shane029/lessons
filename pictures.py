num_dict = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10
}

a = input('a = ')
b = input('b = ')
a_int = 0
b_int = 0
count = 0
number = len(a)
# for j in range(len(a) - 1):
    
for i in a:
    if i in num_dict:
        a_int = a_int + num_dict[i] * number
        

print(a_int + b_int)
