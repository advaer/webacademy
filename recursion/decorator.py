import time


def timer(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print("Time spent: {0} mks".format((t1-t0)*1000000))
        return result
    return wrapper


if __name__ == "__main__":
    @timer
    def test_func(n):
        result = 0
        for i in range(n):
            result += i
        return result

    print(test_func(10))
    print(test_func(1000))
