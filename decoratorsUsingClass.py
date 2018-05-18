def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print 'wrapper executed before this function {}'. format(original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function


#
class decorator_class(object): # object is created here
    # pass original_function to decorator class using init method
    # init function below cretes a class instance as 'self' as well as receives function as argument
    def __init__(self, original_function): # self is used for instance of class
        # assign original_function to instance of a class
        # tie function to the instance of class
        self.original_function = original_function

    # wrapper is implemented using __call__ method. We pass the same argument as well
    def __call__(self, *args, **kwargs):
        # since we are using instance of the class, we have to replace
        # original_function with self.original_function
        print "call method from class executed before {}".format(self.original_function.__name__)
        return self.original_function(*args,**kwargs)


@decorator_class
def display():
    print "display function ran"

@decorator_class
def display_info (name, age):
    print('display_info ran with arguments {}, {}'.format(name,age))

display_info('John', 25)
display()


'''
# output

call method from class executed before display_info
display_info ran with arguments John, 25
call method executed before display
display function ran

'''


'''
# INIT and CALL in python
ref - https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
Defining a custom __call__() method in the meta-class allows the class's instance to 
be called as a function, not always modifying the instance itself.

In [1]: class A:
   ...:     def __init__(self):
   ...:         print "init"
   ...:         
   ...:     def __call__(self):
   ...:         print "call"
   ...:         
   ...:         

In [2]: a = A()
init

In [3]: a()
call

'''
