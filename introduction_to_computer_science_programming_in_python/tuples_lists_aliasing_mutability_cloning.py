# functions
# decomposition – create structure
# abstraction – suppress details
# from now on will be using functions a lot

# tuples are an immutable ordered sequence of elements
#   use () to define them, indexed like arrays
#   singleton (single-value) tupple needs comma to differentiate from list
tuple1 = (1, "Bijan", 123)
# USED TO SWAP VARIABLE VALUES
x = 123
y = 321
(x, y) = (y, x)
print("Respectively, x and y are: ", x, " and ", y, "\n\n")
# USED TO RETURN MORE THAN ONE VALUE FROM A FUNCTION


# example iterating over tuples
def get_data(aTuple):
    fletter = ()
    sletter = ()
    for t in aTuple:
        fletter = fletter + (t[0],)
        if t[1] not in sletter:
            sletter = sletter + (t[1],)
    min_n = min(fletter)
    max_n = max(fletter)
    unique_letters = len(sletter)
    return (min_n, max_n, unique_letters)

tuple2 = ("Hello", "Bobcat", "Hey")
print(get_data(tuple2), "\n\n")

# lists are denoted by []
# common for every index to be of same type (homogenous) but not necessary
# LISTS ARE MUTABLE AND CAN BE CHANGED ONCE ASSIGNED
# can use for i in range(len(list)) to iterate
#   or can use for i in list

# appending to list
a = []
a.append(1)
a.append(10)
print(a, "\n\n")
# the dot comes from the fact that the list is in object (like everythihng in python)
# objects have data, methods, and functions

# can also use +operator to cancatenate 2 lists
#   or .extend to add list to end of list

# EXAMPLES MUTATING LIST
print(a)
del(a[1]) # deletes specified index in a
print(a)

a.append(10)
print(a)

a.remove(10) # looks for value in list and removes indexes with that value
print(a)

# POP WILL REMOVE AND RETURN THE ITEM AT A CERTAIN INDEX
#   DEFAULT IS LAST VALUE
print(a.pop.__doc__, "\n\n")

# can cast string to list with list()
# can use s.split() on string to split string on a character parameter (default space)
# can use ''.join() to turn list into string. '_'.join() will join with _ inbetween

# FOR LIST OBJECT BASIC METHODS
# https://docs.python.org/3/tutorial/datastructures.html

# note that adding and popping from begining of list is very innefecient
#   all elements have to be shifted after this

# quickly creating lists
squares = []
for x in range(10):
    squares.append(x**2)
print(squares, "\n\n")
# creates dummy variable x still WE DON'T NEED THAT
#   here's how to do it without that
squares = []
squares = list(map(lambda x: x**2, range(10)))
print(squares, "\n\n")
squares = []
squares = [x**2 for x in range(10)]
print(squares, "\n\n")
# a lambda function is a small anonymous function with no name
#   take any number of arguments but can only have one expression
#   lambda arguments : expression
x = lambda a, b : a * b
print(x(5, 6), "\n\n")
# map function applies an iterator over this map(function, iterator)

# can make functions that define functions with lambda!
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11), "\n\n")

# is equivalent to a nested for loop and then defining if expression is true for that iteration
test = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(test, "\n\n")

# FOR MORE INFO ON THIS LOOK UP LIST COMPREHENSIONS



# since lists are mutables variables point to value in memory
#   this can have side effects and should always be thought of
#   example here is they both change cause they essentially have the same pointer
warm = ['red', 'yelow', 'blue']
hot = warm
hot.append('purple')
print(hot, "\n")
print(warm,"\n\n")

# creating a new list prevents this
warm = ['red', 'yelow', 'blue']
hot = warm[:]
hot.append('purple')
print(hot, "\n")
print(warm,"\n\n")

# .sort mutates a list and returns nothing while .sorted does not mutate the list and returns the sorted list

# avoid mutating a list while you are iterating over it
#   CLONE FIRST AND REMEMBER THAT L1_COPY=L1 WILL NOT CLONE!
#   NEED L1_COPY=L1[:]