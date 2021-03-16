n = int(input("Enter a number: "))


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0 and n != i:
                return False
    return True


print(is_prime(n))
