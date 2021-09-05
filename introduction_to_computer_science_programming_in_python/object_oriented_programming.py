# ALL DATA IN PYTHON IS AN OBJECT WITH:
#   A TYPE
#   AN INTERNAL DATA REPRESENTATION (PRIMITIVE OR COMPOSITE)
#   A SET OF PROCEDURES FOR INTERACTION WITH THE OBJECT
#   so an object is an instance of a type

# use del to destroy objects
# objects are a data abstraction with internal representation through data attributes
# hids implementation but defines behaviors

# Example list:
#   all of these things are defined internally
#L[i], L[i:j], +
#len(), min(), max(), del(L[i])
#L.append(),L.extend(),L.count(),L.index(),
#L.insert(),L.pop(),L.remove(),L.reverse(), L.sort()

# INCREASED MODULARITY REDUCES COMPLEXITY 
#   EX: TEST BEHAVIOUR OF EACH CLASS SEPERATELY
#   EACH CLASS HAS SEPERATE ENVIRONMENT
#   MANY PYTHON MODULES DEFINE NEW CLASSES

# TO DEFINE A NEW CLASS (YOUR OWN TYPE ESSENTIALLY)
# class Coordinate(object):
#     define attributes here
#     data attributes
#     methods

# DEFINE HOW TO CREATE AN INSTANCE OF OBJECT
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
print(Coordinate(1,2))
print(Coordinate(1,2).x)
print(Coordinate(1,2).y)
# data attributes of a class instance are called instance variable
# python automatically provides argument for self

# methods are like functions can access instance variables called with .
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        """Finds distance between self and another Coordinate object"""
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

a = Coordinate(1, 1)
b = Coordinate(2, 2)
d = a.distance(b)
print(d)

# Python calls the __str__ method when used with print on your class object
# you can choose what it does!

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

c = Coordinate(3,4)
print(c)

# to check what object you are
print(isinstance(c, Coordinate))

# DEFINING SPECIAL OPERATORS
# LIKE PRINT CAN OVERIDE THESE TO WORK WITH YOUR CLASS
#__add__(self, other) -> self + other
#__sub__(self, other) -> self - other
#__eq__(self, other) -> self == other
#__lt__(self, other) -> self < other
#__len__(self) -> len(self)
#__str__(self) -> print self

