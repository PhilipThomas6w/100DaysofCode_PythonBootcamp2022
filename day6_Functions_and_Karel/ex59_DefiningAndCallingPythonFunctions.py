# We define a function by the def keyword.

def my_function1():
    print("This is an imperative statement contained or delimited by the function my_function")
    print("This is also an imperative statement contained or delimited by the function my_function")
    print("If I 'call' the function my_function, each imperative statement contained by it will be processed by the"
          " Interpreter")

my_function1()

# To elaborate: A set of commands or instructions can be delimited by a type of name: in the context of the Python
# language, we call this type of name a "function". Each command delimited or 'contained' by a function represents a
# step 'through' that function: that is, a step 'through' a function can be represented by an imperative statement.
# The Python language requires users to delimit the steps through a function by (means of) indentation, and to delimit
# individual steps by means of line-spaces.

def my_function2():
    print("This is a step through the function my_function2")
    print("This is also a step through the function my_function2")
    print("If I 'call' the function my_function2, each step contained by it will be processed by the"
          " Interpreter")

my_function2()