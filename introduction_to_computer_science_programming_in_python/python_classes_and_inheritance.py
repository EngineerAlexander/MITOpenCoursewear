# MORE ON CLASSES GETTERS AND SETTERS
# INFORMATION HIDING
# CLASS VARIABLES

# self reffers to some instance while defining the class
# object is the class parent
# define this new class animal (child) that inherits all the methods and properties from another class, object (parent)
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

# GETTERS AND SETTERS SHOULD BE USED OUTSIDE OF THE CLASS TO ACCESS DATA ATTRIBUTES!!!
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    
# you can access data values directly with . BUT IT IS NOT RECOMMENDED
# AUTHOR OF CLASS DEFINITION MAY CHANGE DATA ATTRIBUTE VARIABLE NAMES
# THIS CAN PROPOGATE ERRORS OUTSIDE OF CLASS IN CODES WHERE CLASS IS BEING USED

# PYTHON IS NOT GREAT AT INFORMATION HIDING
#   It allows you to access data, write to data, and create data attributes for an instance from outside the class definition
#   DO NOT DO ANY OF THESE!

# DEFAULT ARGUMENTS (USED IF NO ARGUMENT IS GIVEN)
# Class...
def set_name(self, newname=""):
    self.name = newname

# hierarchies of class for inheritance
# child classes can then add more info, add more behavior, or override behavior
# everything should somewhere in the flow inherit the object class
# object class enables the veyr basic operation in python like binding variables, etc.

# PARENT CLASS IS (SUPERCLASS) AND CHILD CLASS IS (SUBCLASS)

# EXAMPLE OF DEFINING A CHILD CLASS CAT TO PARENT CLASS ANIMAL THAT HAD PARENT CLASS OBJECT
# OVERRIDS __str__ and ADDS NEW FUNCTIONALITY via speak method
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

# class variables and their values are shared between all instances of a class
# HERE TAG IS A CLASS VARIABLE
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

# WORKING WITH YOUR OWN TYPES
def __add__(self, other):
    # returning object of same type as this class
    # NEW RABBIT OF AGE O, SELF IS PARENT 1, OTHER IS PARENT 2
    return Rabbit(0, self, other)

#recall Rabbit’s __init__(self, age, parent1=None, parent2=None)

# TO CHECK IF TWO RABBITS HAVE THE SAME PARENTS WITH THE EQUAL SIGN
def __eq__(self, other):
    parents_same = self.parent1.rid == other.parent1.rid \
        and self.parent2.rid == other.parent2.rid
    parents_opposite = self.parent2.rid == other.parent1.rid \
        and self.parent1.rid == other.parent2.rid
    return parents_same or parents_opposite
