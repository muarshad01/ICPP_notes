# Scoping
def f(x): # name x used as 'formal parameter
    y = 1
    x = x + y
    print('x =', x)
    return x

x = 3
y = 2
z = f(x) # value of x used as actual parameter
print('z =', z)
print('x =', x)
print('y =', y)
print('\n')

#####

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z = ', z)
z()
