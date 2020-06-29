#%% Recursion ==============================================================
def iterative_factorial(n):
    """Assumes n an int > 0 Returns n!"""
    result = 1
    
    while n > 1:
        result = result * n
        n -= 1
    return result

print(iterative_factorial(5))
print('------------------\n')

def recursive_factorial(n):
    """Assumes n an int > 0 Returns n!"""
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(4))
print('------------------\n')
    
#%% Fibonacci Numbers
def fib(n):
    """Assumes n int >= 0. Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)

def test_fib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))

test_fib(5)
