def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

chars = '+=-*/'
    
result = 0

number_string = ''
result_num = []
numbers = []
is_multiple = []
count = 0
while True:
    move = input()
    for i in move:
        if i.isalpha() == False and i not in chars:
            number_string += i
            continue
        if i in chars and i != '=':
            count += 1
        numbers.append(int(number_string)) 
        number_string = ''
    for i in move:
        if i == '*':
            result = multiply(numbers[0], numbers[1])
            numbers.remove(numbers[0])
            numbers[0] = result
        elif i == '/':
            result = devide(numbers[0], numbers[1])
            numbers.remove(numbers[0])
            numbers[0] = result
        elif i == '+':
            result = add(numbers[0], numbers[1])
            numbers.remove(numbers[0])
            numbers[0] = result
        elif i == '-':
            result = substract(numbers[0], numbers[1])
            numbers.remove(numbers[0])
            numbers[0] = result    
    print(result)
    numbers = []