def max_val(x, y):
    if x > y:
        return x
    else: 
        return y

print( max_val(7, 4))
print('\n')

###################################################################

def is_in(string1, string2):
    if string1 in string2:
        return True
    elif string2 in string1:
        return True
    else:
        return False

print(is_in('X', 'XY'))
print(is_in('XY', 'Y'))
print(is_in('X', 'Y'))
print('\n')

###################################################################

# Keyword Arguments and Default Values
def print_name(first_name, last_name, reverse):
    if reverse:
        print(last_name + ", " + first_name)
    else:
        print(first_name, last_name)

print_name('Olga', 'Puchmajerova', False)
print_name('Olga', 'Puchmajerova', reverse=False)
print_name('Olga', last_name='Puchmajerova', reverse=False)
print_name(last_name='Puchmajerova', first_name='Olga', reverse = False)
# following throws error: 
# print_name('Olga', last_name='Puchmajerova', False)
print('\n')

###################################################################

def print_name(first_name, last_name, reverse = False):
    if reverse:
        print(last_name + ", " + first_name)
    else:
        print(first_name, last_name)

print_name('Olga', 'Puchmajerova')
print_name('Olga', 'Puchmajerova', True)
print_name('Olga', 'Puchmajerova', reverse=True)
print('\n')