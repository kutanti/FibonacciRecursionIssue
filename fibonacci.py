# this function  computes the nth term of fibonacci series with recursion
def fibonacciWithRecurssion(n):
    fibonacci_cache = {}
    if n < 0:
        print("Incorrect input")
        return -1
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    value = 0
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacciWithRecurssion(n-1)+fibonacciWithRecurssion(n-2)
    fibonacci_cache[n] = value
    return value


# this function  computes the nth term of fibonacci series without recursion


def fibonacciWithourRecusrrion(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


# printing the first fifty numbers in fibonacci series, it will fail
for i in range(1, 50):
    print(str(i)+":"+str(fibonacciWithRecurssion(i)))

# printing the first thousand numbers in fibonacci series, it compute smoothly
for i in range(1, 1001):
    print(str(i)+":"+str(fibonacciWithourRecusrrion(i)))
