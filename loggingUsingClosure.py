# logging with closure in Python
# In simple terms a closure is an inner fucntion that rememebr and has access to variables in local scope in which it (inner fucntion)
# has been created, even when outer function has finished executing.


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y


def logger(func):

    # Following function accepts any number of arguments and logs the details
    # like function name and argument details. It also actually runs the function
    # and prints the result to console. (not to the log file)
    def log_func(*args):    # we can pass any number of arguments to inner function
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print func(*args)
    return log_func

# we are trying to get the pointer to inner function, while we also pass the function to be called in future
# However due to closure property, inner function remembers which function was passed earlier to outer function
add_logger = logger(add)
sub_logger = logger(sub)

# inner function already knows what function they should call (add/sub). This is closure property.
add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)


'''
The code generates the example.log file. It looks like this,
INFO:root:Running "add" with arguments (3, 3)
INFO:root:Running "add" with arguments (4, 5)
INFO:root:Running "sub" with arguments (10, 5)
INFO:root:Running "sub" with arguments (20, 10)
INFO:root:Running "add" with arguments (3, 3)
INFO:root:Running "add" with arguments (4, 5)
INFO:root:Running "sub" with arguments (10, 5)
INFO:root:Running "sub" with arguments (20, 10)


'''
