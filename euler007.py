#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def nthprime(n):
    nthprime = 0
    number = 1
    while nthprime < n:
        number += 1
        if isprime(number):
            nthprime += 1
    return number


print(nthprime(10001))
