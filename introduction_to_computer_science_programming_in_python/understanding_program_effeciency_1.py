# measuring orders of growth of algorithms
# big "Oh" notation and complexity classes
# seperate time and space efficiency of a program and tradeoff between them
# will focus on time effeciency

# to evaluate effeciency:
#   MEASURE WITH A TIMER
#   COUNT THE OPERATIONS
#   ABSTRACT NOTION OF ORDER OF GROWTH! (arguably the most appropriate way to go about it)

# to time a program. note varies by machine, implementations, not predictable based on small inputs
# very usefull for comparing algorithms
import time

def c_to_f(c):
    return c*9/5 + 32
t0 = time.perf_counter()
c_to_f(100000)
t1 = time.perf_counter() - t0
print("dt =", t1)

# examples counting operations
# assume they take equal time: mathematical operations, comparisons, assignments, accessing objects in memory
# is better but still has downsides like depends on implementations and not clear which operations to count

def c_to_f(c):
    return c*9.0/5 + 32 # 3 operations

def mysum(x):
    total = 0 # 1 operation
    for i in range(x+1): # everything in this loop x times. 1 operation here
        total +=i # 2 operations (increment and assignment)
        return total
    
print(mysum(10)) # using function with x gives 1+3x operations!

# BEST WAY EVALUATE ALGORITHM, EVALUATE SCALABILITY, EVALUATE IN TERMS OF INPUT SIZE!
#   FOCUS ON HOW ALGO PERFORMS WHEN SIZE OF PROBLEM GETS ARBITARILY LARGE
#   DECIDE WHAT YOUR INPUT IS: INT, LENGTH OF LIST, ETC., YOU DECIDE especially when multiple params to a function!

def search_for_elmt(L, e):
    for i in L:
        if i == e:
            return True
    return False
# when e is	first element in the list BEST CASE	
# when e is	not in list WORST CASE	
# when look through about half of the elements in list AVERAGE CASE

# GENERALLY WILL FOCUS ON WORST CASE SCENARIO
#   This is O(n) growth below since it's like a 1 + 5n + 1 depending on input size
#   Ignore additive and multiplicative constants - we don't care about them
#   If you have something like n^2 + 2n + 2 FOCUS ON DOMINATE TERMS! This would be O(n^2)
#   From best to worst: O(1), O(log(n)), O(n), O(nlog(n)), O(n^2), O(2^n), O(n!)

def fact_iter(n):
    """assumes n an int >= 0"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

# COMBINE COMPLEXITY CLASSES
#   LAW OF ADDITION FOR O(): used with sequential statements O(f(n)) + O(g(n)) is O(f(n) + g(n))
#   EXAMPLE:
# for i in range(n):
#     print('a')
# for j in range(n*n):
#     print('b')
#   is O(n) + O(n*n) =	O(n+n^2) = O(n^2) because of dominant term
#   LAW OF MULTIPLICATION OF O(): used with nested statements/loops
#   O(f(n)) * O(g(n)) is O(f(n) * g(n))
#   EXAMPLE:
# for i in range(n):
#     for j in range(n):
#         print('a')
#   is O(n)*O(n) = O(n*n) = O(n2)

# DENOTATIONS OF COMMON RUNTIMES
# O(1) denotes constant running
# O(log n) denotes logarithmic running 
# O(n) denotes linear running 
# (n log n) denotes log-linear running 
# O(n^c) denotes polynomial running (c is a constant)
# (c^n) denotes exponential running (c is a constant being raised to a power based on size of input)

# Linear Search
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
# O(n) where n is len(L)

# Linear Search on SORTED LIST
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
# O(n) where n is len(L) BUT RUNTIME CAN BE DIFFERENT

# SEARCHING A LIST IN SEQUENCE TO SEE IF AN ELEMENT IS PRESENT HAS LINEAR COMPLEXITY

# QUADRATIC COMPLEXITY
#   CHECKING IF L1 IS A SUBSET OF L2
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
# REMEMBER WE CARE FOR WORST CASE: O(n^2)

#   CHECKING IF THERE IS AN INTERSECTION (SAME ELEMENT)
def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
#   ASSUMING LISTS ARE ROUGHLY THE SAME LENGTH, O(len(L1)^2)=O(n^2)

# THIS ALGO CUMPUTES N^2 VERY EFFECIENTLY
#   when dealing with nexted loops look at the ranges for O
def g(n):
    """ assume n >= 0 """
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x