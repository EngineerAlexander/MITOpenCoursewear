# SEMANTICS TO REMEMBER ---------------------------------------------

# input() gives string so cast if appropriate

text = input("Type anything... ")
print(5*text)

# for loop structure
start = 0
step = 1 # these two optional

stop = 3 # end value

range(start,stop,step)

# for loops can always be re-written with while loops but not vice versa

# string indexing
# default: [start:stop:step], step = 1
# two input: [start:stop]

# strings are immutable and cannot be modified
# bottom works cause s bound to new object
s = "hello"
s = 'y'+s[1:len(s)]
print(s)

# strings can also be indexed with [start:stop:step]
print(s[::]) #all forwards
print(s[::-1]) #all backwards
# note can omit step (last index) too

# for loops can iterate over any set of values (ex. strings)5