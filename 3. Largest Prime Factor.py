"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

>>>6857
"""


def solution1(n):
    """
    This function returns list of prime factors.
    (This is my own solution... but it is complicated and slow)
    """

    def find_next_prime_factor(startIndex):
        """
        Find the next valid prime factor with given startIndex(inclusive)
        """
        while True:
            for y in range(2, startIndex):
                if not startIndex % y:
                    break
            else:
                return startIndex
            startIndex += 1

    testNum = n
    factorNum = 1
    result = []

    while True:
        factorNum = find_next_prime_factor(factorNum + 1)
        while not testNum % factorNum:
            testNum /= factorNum
            result.append(factorNum)
            if testNum == 1:
                break
        else:
            continue

        break

    return(max(result))

def solution2(n):
    """
    This function returns only the largest prime factor.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def solution3(n):
    """
    This function returns list of prime factors.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(solution1(600851475143))

