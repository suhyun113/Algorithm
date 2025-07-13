def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

N = int(input())
if N == 0:
    result = 1
else:
    result = factorial(N)

print(result)