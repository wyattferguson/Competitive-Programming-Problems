'''
Name: Sum square difference
Problem URL: https://projecteuler.net/problem=6
Date Completed: 2019 

Description:
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

n = 100
a_sum = (n*(n+1)/2) ** 2  # square of the sum formula
b_sum = 0
for k in range(1, n+1):
    b_sum += k ** 2

print(abs(a_sum - b_sum))
