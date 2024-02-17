


def display_fib(n):
    if n == 0:
        return [0]

    if n == 1:
        return [0, 1]

    fib_list = [0, 1]
    a, b=0, 1

    for i in range(2, n):
        c = a + b
        fib_list.append(c)
        a = b
        b = c

    return fib_list

n = 10
print(display_fib(n))
