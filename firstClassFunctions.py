#First class fucntions

def adder(number):
    return number + number;

def square(x):
    return x * x

def cube(x):
    return x * x * x

def simple_square(arg_list):
    result = []
    for i in arg_list:
        result.append(i*i)
    return  result;


def mapping_first_class(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))  # func variable is passing during function call

    return result


numbers = [1,2,3,4,5]
print "numbers: ", numbers

# This is simple call to the function func_square
result = simple_square(numbers)
print "Simple square call: " , result

# Following line illustartes concept of first class functions.  We call function func_square. Along with that we also tell the fucntion
# which fucntion to call, here we are calling "adder". We also pass the arguments to the fucntion as arg_list.
result = mapping_first_class(adder, numbers)    # just pass the fucntion name
print "Calling the adder function from function: ", result

result = mapping_first_class(square, numbers)
print "Calling the square function from function: ", result

result = mapping_first_class(cube, numbers)
print "Calling the cube function from function: ", result

