# Defensive programming
#   involves writing specifications for functions
#   modularizing programs
#   check conditions on inputs/outputs (assertions)

#   testing/validation
#       compare input/output pairs to specs
#       think how can i break my program

#   debugging
#       study events leading up to an error
#       how can i fix my program

# FROM THE START DESIGN CODE THIS WAY!!
# BREAK CODE UP INTO MODULES THAT CAN BE TESTED AND DEBUGGED INDIVIDUALLY
# DOCUMENT CONSTRAINTS ON MODULES FOR INPUT/OUTPUT
# DOCUMENT ASSUMPTIONS BEHIND THE CODE DESIGN
# WHEN READY TO TEST, ENSURE CODE RUNS, HAVE EXPECTED RESULTS SET
#   AN INPUT SET, FOR EACH INPUT, AN EXPECTED OUTPUT

# CLASSES OF TESTS
# Unit Testing: validate each piece of program, testing functions seperately
# Regression Testing: add tests for bugs as you find them
#   catch reintroduced errors that were previously fixed
# Integration Testign: does overall program work
#   prevent urge to rush to this step

# use intiution about natural boundaries to the problem
#   without natural partitions, can do random testing
#   many random tests, higher probability the code is correct

# black box testing
#   explore paths through specification
#       build test cases in different natural space partitions
#       consider boundary conditions/fringe cases
#           empty lists, singleton list, large nums, small nums
#   designed without looking at the code
#   testing integer/float extremes

# ex:
# CASE    x   eps
# boundary 0   0.0001
# perfect square 25    0.0001
# less than 1 0.05     0.0001
# irrational square root 2     0.0001
# extremes 2   1.0/2.0**64.0
# extremes 1.0/2.0**64.0   1.0/2.0**64.0
# extremes 2.0**64.0   1.0/2.0**64.0
# extremes 1.0/2.0**64.0   2.0**64.0
# extremes 2.0**64.0   2.0**64.0


# glass box testing
#   explore paths through code
#   code guides design of test cases
#   path-complete if every potential path through code is tested at least once
#   can miss paths, or go through loops a bunch of times
#   a path complete test suite can still miss a bug and you should still test boundary conditions

# EASY ERROR MESSAGES TO FIX
# trying to access beyond the limits of a list
# test = [1,2,3] then test[4] IndexError
# trying to convert an inappropriate type
# int(test) TypeError
# referencing a non-existent variable
# a NameError
# mixing data types without appropriate coercion
# '3'/4 TypeError
# forgetting to close parenthesis, quotation, etc.
# a = len([1,2,3]
# print(a) SyntaxError

# LOGIC ERRORS ARE MUCH HARDER TO FIX!

# WAY TO DEAL WITH EXCEPTIONS with handlers
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except:
    print("Bug in user input.")
    # any exception raised in try are handled by the scept statement
    # execution continues

# CAN BE MORE SPECIFIC HANDLING EXPECTIONS LIKE THIS
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except TypeError:
    print("Mixing data types without coercion")
except:
    print("Something went very wrong.")
# can follow this with else: to execute when try completes with no exceptions
# can use finally: which is always executed after all clauses
#   usefull for doing stuff that should always run (ex. closing file)

# WHAT TO DO WITH EXCEPTIONS
# should return an error value
# or should stop execution and signal error condition
# raise Exception("The bull run is over!")
# can be more specific
# raise ValueError("Something is wrong")

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = not a number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

# except: gets executed here becaue of indexing access error
#a = [1, 2]
#b = [2]
#get_ratios(a, b)

# gets nan values note it's a special type of float so can be converted to float
# except: doesn't execute
#a = [1, 2]
#b = [0, 0]
#print(get_ratios(a, b))

# good to write code that will flag errors and then procede

# ASSERTIONS ARE USED TO CHECK ASSUMPTIONS ARE AS EXPECTED
# ASSERT STATEMENT WILL RAISE AN ASSERTIONeRROR expection if assumptions not met
# THIS IS GOOD DEFENSIVE PROGRAMING!

def avg(grades):
    assert len(grades) != 0, 'no grades data'
    return sum(grades)/len(grades)
# if empty list for grades raises an AssertionError and ends immediately
# typically used to check inputs to functions
# can be used to check outputs of a function too
# ensures that execution halts whenever an expected condition is not met
# assertions don't allow you to control response to unexpected conditions

#   use as a supplement to testing
#   raise exceptions if users supplies bad data input
#   use assertions to
#   check types of arguments or values
#   check that invariants on data structures are met
#   check constraints on return values
#   check for violations of constraints on procedure (e.g. no
#   duplicates in a list)

