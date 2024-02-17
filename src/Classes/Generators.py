def gen_top_ten():
    n = 1
    while n <= 10:
        sq = n * n
        n += 1
        yield sq


top_ten = gen_top_ten()

for i in top_ten:
    print(i)





"""
Exception
"""

a = 10
b = 0

try:
    print("Resource open")
    print(a/b)
except Exception as e:
    print("[Can't divide by 0]", e)
finally:
    print("Resource closed")