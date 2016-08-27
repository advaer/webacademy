import sys

default_limit = sys.getrecursionlimit()
print("Default limit:", default_limit)

sys.setrecursionlimit(2000)

updated_limit = sys.getrecursionlimit()
print("Updated limit:", updated_limit)