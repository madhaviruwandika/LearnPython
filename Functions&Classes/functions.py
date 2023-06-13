#Functions
## Defined with def
## end of definition : should be added and body should be added with correct indentation
print('-------------------------Functions-----------------------------')
def my_function(val1, val2):
    print("my function output : ", val1*val2)

# bellow will retun None as no value is returned. equal to  undefined
print(my_function(2,10))

print("\n-------------Factorial Function----------------")
def factorialWithRecurtion(intVal):

    if(type(intVal) is not int):
        return None;
    if(intVal < 0):
        return None;

    if(intVal == 0):
        return None;

    if(intVal == 1):
        return 1;

    return intVal * factorial(intVal-1);

def factorial(intVal):

    if(type(intVal) is not int):
        return None;
    if(intVal < 0):
        return None;

    if(intVal == 0):
        return None;

    val_factorial = 1
    while(intVal > 0):
        val_factorial = val_factorial * intVal;
        intVal = intVal - 1;
    return val_factorial;

print('Factorial(1) =', factorial(1))
print('Factorial(5) =', factorial(5))
print('Factorial(6) =', factorial(6))
print('Factorial(0) =', factorial(0))
print('Factorial(-2) =', factorial(-2))
print('Factorial(1.2) =', factorial(1.2))
print('Factorial("abc") =', factorial("abc"))

print("\n-------------Arguments and Keyword arguments----------------")
# Arguments and Keyword arguments
def example_1(*args, **kwargs):
    print(args)
    print(kwargs)
    print(locals())

example_1(2,3,5, operation1='key 1', operation2='key 2')

#function of functions
print("\n-------------function of functions----------------")

def example_2():
    var1 = 5
    var2 = 6
    def example_sum(var1, var3):
        ##var2 is taken from globle variables
        print('var1+var2', var1+var2)
        print('var1+var3', var1+var3)

    example_sum(var1,7)

example_2()

# Lambda functions
print("\n-------------Lambda functions----------------")

print('This is  lambda function output: ',(lambda x: x+5)(1))