from itertools import product

A = [1, 2, 3]
B = [4, 5, 6]
C = [7, 8, 9]

cart = [(a, b) for a in A for b in B]
cart2 = [(a, b, c) for a in A for b in B for c in C]

print(cart)
print(cart2)


# Enter your code here. Read input from STDIN. Print output to STDOUT

a = input().split(' ')
b = input().split(' ')

a = [int(x) for x in a]
b = [int(x) for x in b]

for x in list(product(a, b)):
    print(x, end=' ')
