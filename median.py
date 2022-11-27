def median(a, b, c : int) -> int:
    if a >= b:
        if b >= c:
            return b
        else:
            return c
    elif a >= c:
        return a
    else:
        return c
    
    
def main():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print(median(a, b, c))
    
if __name__ == "__main__":
    main()