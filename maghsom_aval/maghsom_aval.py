# Python program to print prime factors
import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    list_of_prime = []
    counter=0
    # Print the number of two's that divide n
    while n % 2 == 0:
        if 2 not in list_of_prime:
            list_of_prime.append(2)
            counter += 1
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            if i not in list_of_prime:
                list_of_prime.append(i)
                counter+=1
            n = n / i

        # Condition if n is a prime
    # number greater than 2
    if n > 2:
        if n not in list_of_prime:
            list_of_prime.append(n)
            counter += 1

    return counter

    # Driver Program to test above function

def main():
    number = 0
    prime_factor = 0
    for i in range(10):
        num = int(input())
        num_of_factor = primeFactors(num)
        if num_of_factor > prime_factor:
            prime_factor = num_of_factor
            number = num
        elif num_of_factor == prime_factor:
            if num > number:
                number = num
    print(number,prime_factor)

if __name__== "__main__":
    main()