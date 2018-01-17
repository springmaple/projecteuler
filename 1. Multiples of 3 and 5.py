"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

>>>233168
"""
def solution1(MAX_SIZE):
    return sum((x for x in range(MAX_SIZE) if not x % 5 or not x % 3))

print(solution1(MAX_SIZE=1000))
