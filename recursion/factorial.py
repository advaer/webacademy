def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

result1 = fact(3)
print(result1)

result2 = fact(4)
print(result2)

print(fact(5))
