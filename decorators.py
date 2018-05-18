# Decorator is a just function which takes another function as an argument, add some kind of functionality and returns another 
# fucntion; all of these without altering the source code of the original function that is passed in.

# purpose: decorating the function allows us to easily add functionality to existing function by adding that 
# functionality inside the wrapper.

'''
# Basic decorator function

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print "display function ran"

decorator_display = decorator_function(display)

decorator_display()

'''

# without modifying our original display function in any way, 
# I can come inside wrapper and add any code I want. example, print statement added 'wrapper executed before this'.
# { } this is called placeholder for __name__

'''
# Modify Basic decorator function

def decorator_function(original_function):
    def wrapper_function():
        print 'wrapper executed before this function {}'. format(original_function.__name__)
        return original_function()
    return wrapper_function

def display():
    print "display function ran"

decorator_display = decorator_function(display)

decorator_display()

'''


'''
# NEW SYNTAX



def decorator_function(original_function):
    def wrapper_function():
        print 'wrapper executed before this function {}'. format(original_function.__name__)
        return original_function()
    return wrapper_function

# display() function is now surrounded by decorator_function. Whenever we call display() function, it is equivalent to calling following 
# 2 lines. These 2 lines are very similar to  putting @decorator_function before display() defination. This syntax is useful when we 
# want to chain multiple decorators.
#decorator_display = decorator_function(display)
#decorator_display()


@decorator_function             
def display():
    print "display function ran"

#decorator_display = decorator_function(display)

#decorator_display()

display()

'''


'''
# Decorate multiple functions with same decorator function
# we have to make use of *args and **kwargs variable
# wrapper function accepts 2 additional but optional arguments. The same arguments are added in return call as well.
# But the defination of the decorator_function remains the same. ??? We do not add these parameter to syntax of decorator function,
# but we add these parameters to defination of wrapper functions.

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):      # see the parameters added
        print 'wrapper executed before this function {}'. format(original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print "display function ran"

@decorator_function
def display_info (name, age):
    print('display_info ran with arguments {}, {}'.format(name,age))

display_info('John', 25)
display()


'''




















'''import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
'''
