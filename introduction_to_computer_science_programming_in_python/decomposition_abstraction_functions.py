# in programing divide code into self-contained modules
#   they are easy to break up, reusable, organized, keep coherent code
# functions (discussed here) and classes do this
# be sure to use docstrings and can call them as such
print("Using .__doc__:\n")
print(min.__doc__)
# or
print("\n\n\nUsing help function:\n")
help(min)

# functions are called or invoked and they have
#   name, params, docstring, body, return

def is_even(x):
    """
    Input: any integer x
    Returns: 1 if even, 0 if odd
    """
    if isinstance(x, int):
        return x%2==0
    else:
        print("Number is not an integer")
        return

print(is_even(.1),"\n")
print(is_even(2),"\n")
print(is_even(3),"\n\n\n")

# python returns value "None" if no return is given
# represents absence of a value

# scope of variables in functions is internal to functions
# variables get passed back and force

# function arguments can be any type even other functions

# functions can access variables defined in higher scope that called the function
#   they cannot modify these variables
#   can modify if global variables but is frowned upon

# unboundedlocalerrors

# use http://www.pythontutor.com/ to visualize flow

