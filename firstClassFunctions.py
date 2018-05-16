#First class fucntions

def adder(number):
    return number + number;

def func_square(arg_list):
    result = []
    for i in arg_list:
        result.append(i*i)
    return  result;


def func_square_first_class(func, arg_list):
    result = []
    for i in arg_list:
        result.append(adder(i))

    return result


numbers = [1,2,3,4,5]
print(numbers)

# This is simple call to the function func_square
result = func_square(numbers)
print "Simple call: " , result

# Following line illustartes concept of first class functions.  We call function func_square. Along with that we also tell the fucntion
# which fucntion to call, here we are calling "adder". We also pass the arguments to the fucntion as arg_list.
result = func_square_first_class(adder, numbers)
print "Calling the adder function from function: ", result


