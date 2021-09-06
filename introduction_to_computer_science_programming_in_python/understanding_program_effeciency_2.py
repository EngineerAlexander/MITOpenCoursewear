# LOG COMPLEXITY
# EX. BISECTION SEARCH, BINARY SEARCH OF LIST

# WHAT IS BISECTION SEARCH
# Sorted list, pick an index i that divides list in half, ask if L[i] == e, depending on answer search left or right
# essentially breaks list into smaller list initially then over and over again
# first list n elements, next n/2, then n/4, n/8, ... n/2^i finish looking through list when 1 = n/2^i aka there's one elmenet left after i iterations
# so i = log(n), where i is the number of iterations
# O(log(n))


# ATTEMPT 1
def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2 # note the integer division (floor division) rounds down
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)
# THE BISECTION SEARCH CALLS ARE OF O(log(n)) since above reason each time they are cut in half
# BUT IN EACH BISECT_SEARCH1 CALL WE ARE COPYING LIST ON THE ORDER OF O(.5n)=O(n)
# Multiplication gives O(nlog(n)), the n dominates. If we are carefull we can do better

# you can speed t his up considerably if you avoid copying the list
# THIS SPEEDS up still O(log(n)) bisection search calls since each time size range is cut in half
# List is never copied!, just re-passed as a pointer O(1) work on each recursive call
# SO O(log(n)) TOTAL ORDER!
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1) # constant other than recursive call
        else:
            return bisect_search_helper(L, e, mid + 1, high) # constant other than recursive call
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
    
# ANOTHER EXAMPLE LOGARITHMIC COMPLEXITY
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    res = '' # everything above this is constant order
    while i > 0:
        res = digits[i%10] + res
        i = i//10 # i will degrade to zero at 100, 10, 1, 0. how many times can one divide i by 10? O(log(i))
    return res

# REMEMBER ITERATIVE LOOPS AND SEARCHING A LIST IN SEQUENCE FOR AN ELEMENT HAS LINEAR COMPLEXITY

# FOR ITERATIVE FACTORIAL FUNCTION
def fact_iter(n):
    prod = 1
    for i in range(1, n+1): # O(n) from loop with constant cost inside it so O(n)
        prod *= i
    return prod

# RECURSIVE FACTORIAL FUNCTION
def fact_recur(n):
    """ assume n >= 0 """
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n-1) # Will call n times just like a loop, O(n)
# the iterative and recursive factorial implementations are the same order of growth

# MANY PRACTICAL ALGOS ARE LOG-LINEAR (VERY COMMON ONE IS MERGE SORT!)

# MOST COMMON POLYNOMIAL ALGORITHMS ARE QUADRATIC O(n^2)
# commonly occurs when there are nested loops or recursive function calls

# EXPONENTIAL COMPLEXITY
# recursive functions with more than one calls for each size of input problem
# many important problems are exponential with very high cost
# can consider approximate solutions as they may provide reasonable answer more quickly
#   EXAMPLE: TOWERS OF HANOI O(2^n)
#   EXAMPLE: Generate the collection of all possible subsets of a set - called the power set

# {1,2,3,4} would generate...
# {},{1},{2},{3},{4},{1,	2},{1,3},{1,4},{2,3},{2,4},{3,4},
# {1,2,3},{1,2,4},{1,3,4},{2,3,4},{1,2,3,4}
# ORDER DOESN'T MATTER
# think recursion. you want to generate all power sets for integers 1 to n. assume you can generate all power sets for 1 to n - 1
# then power set for 1 to n is just all of those subsets and then also all of those subsets with n added to them

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] # list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
    return smaller+new # combine those with last element and those without

print(genSubsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]))
# TO DEDUCE COMPLEXITY:
# tn denotes time to solve problem of size n, sn denotes size of solution for porblem of size n
# tn = tn-1 + sn-1 + c where c is constant number of operations
# can keep expanding this out for plugging in tn-1, etc.
# turns into 1 + 2^n + nc so complexity is exp O(2^n)

# COMPLEXITY CASE CHEAT SHEET
# O(1) – code does not depend on size of problem
# O(log n) – reduce problem in half each time through process
# O(n) – simple iterative or recursive programs
# O(n log n) – will see next 
# O(n^c ) – nested loops or recursive calls
# O(c^n) – mul;ple recursive calls at each level

# Recursive Fibonacci
def fib_recur(n):
    """ assumes n an int >= 0 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2) # if 1 -> 1 calls, if 2 -> 2 calls, if 3 -> 2^2 calls. so O(2^n)
# actually can do a bit better since drawing out function calls there are repeats down the line, but still O(2^n) worst case
    
# know differences between average case and worst case
# can look up complexity of common python functions

