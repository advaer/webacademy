def fact_loop(n):
    fact = 1
    x = 1
    while x <= n:
        fact = fact * x
        x = x + 1
    return fact

result1 = fact_loop(3)
print(result1)

result2 = fact_loop(4)
print(result2)

print(fact_loop(5))
