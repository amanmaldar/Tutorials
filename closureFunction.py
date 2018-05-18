# closure functions and variables.
# closure takes advantage of first class functions.
# closure returns the inner function that remembers and has access to variables local to the scope (scope defined by outer fucntion)
# in which they (inner function and variables) were created.
# In simple terms a closure is an inner fucntion that rememebr and has access to variables in local scope in which it (inner fucntion)
# has been created, even when outer function has finished executing.

def add(x,y):
    return x+y

def outer_func(msg):
    message = msg
    def inner_func():
        print message

    return inner_func

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

# these functions actually remember the values previous passed to outer functions.
# so when we call a function by putting brackets () next to the pointer. The inner_func() gets called
# and it prints previous values
hi_func() 
hello_func()

#output
#Hi
#Hello


'''
# removing the middle man

def outer_func(msg):
    # message = msg # removed this
    def inner_func(msg):
        print message

    return inner_func

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

hi_func() 
hello_func()

#output
#Hi
#Hello
'''
