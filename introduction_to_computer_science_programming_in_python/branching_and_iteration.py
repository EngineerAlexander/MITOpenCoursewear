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

# for loops can iterate over any set of values (ex. strings)

cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
if guess**3 < cube :
low = guess
else:
high = guess
guess = (high + low)/2.0
num_guesses += 1
print 'num_guesses =', num_guesses
print guess, 'is close to the cube root of', cube