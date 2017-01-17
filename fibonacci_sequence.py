def fib(n): # returns fibonacci series up to n
    """
    Return a list containing the Fibonacci series up to n.
    """
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
data = int(input("Enter the upper range: "))
print(fib(data))
