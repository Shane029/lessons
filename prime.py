def is_prime(x : int) -> bool:
    if x <= 3:
        return x
    if x % 2 == 0 or x % 3 == 0:
        return False
    end = int(x ** 0.5)
    for i in range(5, end + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True
def main():
    count = 0
    number = int(input('N = '))
    for i in range(2, number):
        if is_prime(i):
            count += 1
    print(count)
    

if __name__ == "__main__":
    main()
