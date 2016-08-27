def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

result1 = power(2, 4)
print(result1)

result2 = power(3, 7)
print(result2)
