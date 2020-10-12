# Global variable
"""
variables that are created outside of a function are known as global variables.
global variables can be used by every one,both inside and ouside of functions.
"""
# example
x = "boss"
def function1():
   print("praveen is "+x)

function1()
"""
 if you create a variable with same name inside a function,the variable will be a loacl variable and can only be used inside the function.\n"
 global variable with the same name will remain as it was global and with the original value.
 """
#example
x = "awesome"
def function2():
 x = "fantastic"
 print("python is "+x)

function2()



# global keyword:
"""
normally when you create a variable inside a function,that variable is local and can only use inside.
to create a global variable inside function ,you can use global keyword.
if you use global keyword the variable belongs to global scope:
 """
# example
x = "awesome"
def function3():
 global x
 x="superb"
print("rahul is "+x)
print(x)

function3()
print(x)



"""
also use the global keyword if you want to change a global variable inside a function.
"""
# example

