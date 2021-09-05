# BISECTION SEARCH EXAMPLE
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

# interval bounds change each iteration and new guess is halfway inbetween
# this is an example of a log2N complexity
# guesses in order N/2,N/4,N/8,...
# works when function varies monotonically with input

# if negative roots problems arise be sure to properly define range
cube = -27
epsilon = 0.01
num_guesses = 0
low = min(cube,0)
high = max(cube,0)
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

# if |x|<1 and negative this breaks down.
cube = -.01
epsilon = 0.000001
num_guesses = 0
low = min(cube,0)
high = max(cube,0)
guess = (high + low)/2.0
if abs(cube)<1:
    low = -1
    high = 1
    guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

