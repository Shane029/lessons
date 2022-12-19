#  1 cent
#  5 cent
#  10 cent
#  25 cent

'''AMOUNT OF COINS'''

# def money_count(count : int, amount : int) -> bool:
#     if count > 0:
#         return money_count(count - 1, amount - 25) or money_count(count - 1, amount - 10) or money_count(count - 1, amount - 5) or money_count(count - 1, amount - 1)
#     return count == 0 and amount == 0

# def main():
#     count = int(input('Count = '))
#     amount = int(input('Amount = '))
#     print(money_count(count, amount))
# if __name__ == "__main__":
#     main()
    
    
'''Decoding'''

def decoding(code : list, decode = [], count = 0) -> list:
    if count == len(code):
        decode = ''.join(decode)
        decode = list(decode)
        return decode
    else:
        decode.append(code[count] * code[count + 1])
        return decoding(code, decode, count + 2)
def main():
    print(decoding(['a', 5, 'b', 6]))

if __name__ == "__main__":
    main()