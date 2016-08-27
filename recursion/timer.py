from decorator import timer


@timer
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


@timer
def fact_loop(n):
    fact = 1
    x = 1
    while x <= n:
        fact = fact * x
        x = x + 1
    return fact

print(fact(10))
print(fact_loop(10))