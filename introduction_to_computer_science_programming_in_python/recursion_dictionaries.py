# example sol with iteration:
#   multiply a and b is equivalent to add a to itself b times
def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(multi_iter(7, 10))

# example sol with recursion
#   think how to simplify problems (repeated parts) until you rach a simple base case
#   ex: a*b = a+a+a+a b times
#           = a +      a + a + a b-1 times

def multi_recur(a, b):
    if b == 1:
        return a
    else:
        return a + multi_recur(a, b-1)

print(multi_recur(7, 10), "\n\n")
# note that base case will break the infinite loop and is bound to happen
#   note only valid for positive integers


# factorial recursion example

def factorial_recur(a):
    if a == 1:
        return 1
    else:
        return a * factorial_recur(a-1)

print(factorial_recur(3))
print(factorial_recur(8), "\n\n")

# note that each recursive call creates its own scope/environment
#   they are the same variable names but different objects in different scopes
#   control flow will bass function value back up when call returns a value

# RECURSION CAN BE EFFECIENT OR NOT EFFECIENT

# USE INDUCTIVE REASONING TO DETERMINE IF RECURSION WILL WORK
#   reasoning that the base case will always be reached no matter what
# MATHEMATICAL INDUCTION REQUIRES PROVING:
#   1. Prove it is true when n is the smallest value it will reach
#   2. Prove it is true for any arbitrary n
#   3. Then can show that it must be true for n+1

# example using formula (n(n+1))/2=
#   0 + 1 + 2 + 3 + 6 + ... + n
#   1. for 0: 0 = 0
#   2. assume true for k: k(k+1)/2 = 0 + 1 + 2 + ... + k
#   3. need to show that it's true for k+1: (k+1)(k+2)/2 = 0 + 1 + 2 + ... + k + (k+1)
#   4. can show this with algebra, then holds for all n >=0

# a dictionary is a key-value pair
my_dict = {}
student_grades = {'Ana':'B', 'Joe':'C'}
print(student_grades['Joe'])
# can add a pair
student_grades['Bob'] = 'F'
print(student_grades)
# can use del to delete
del(student_grades['Bob'])
print(student_grades)
# test if key in dict
print('Bob' in student_grades)
print('Ana' in student_grades)
# get an iterable as a tuple of all keys
print(student_grades.keys())
# get an iterable as a tuple of all values
print(student_grades.values(), "\n\n")

# VALUES CAN BE ANY TYPE IMMUTABLE OR MUTABLE
# DICT VALUES CAN BE LISTS EVEN DICTIONARIES
# KEYS MUST BE UNIQUE AND IMMUTABLE TYPE
# no order to keys or values! This is valid
d = {4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44]}


# example using dicts to get determine frequency of words on song
lyrics = """They say oh my God I see the way you shine
Take your hand, my dear, and place them both in mine
You know you stopped me dead while I was passing by
And now I beg to see you dance just one more time
Ooh I see you, see you, see you every time
And oh my I, I, I like your style
You, you make me, make me, make me wanna cry
And now I beg to see you dance just one more time
So they say
Dance for me, dance for me, dance for me, oh, oh, oh
I've never seen anybody do the things you do before
They say move for me, move for me, move for me, ay, ay, ay
And when you're done I'll make you do it all again"""

def rm_stuff(string, list):
    for i in list:
        string = string.replace(i, '')
    return string

def freq_dict(string,dict):
    string = string.lower()
    replace_list = [',', '\'']
    string = rm_stuff(string, replace_list)
    words = string.split()
    for word in words:
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
    return dict


freq_mapping = {}
freq_dict(lyrics,freq_mapping)
print(freq_mapping, '\n')

# cast to list and sort
sort_dict = sorted(freq_mapping.items(), key=lambda x: x[1], reverse=True)
print(sort_dict)
print(sort_dict[0])
# note that dictionaries are ordered in python 3.6 unlike earlier!!!
#   however this is returning a sorted list of tuples
print(type(sort_dict),"\n\n")

# print max key:value
max_key = max(freq_mapping, key=freq_mapping.get)
print(max_key)
print(freq_mapping[max_key], "\n\n")
# note can potentially run into problem if there's multiple max values

# fib recursive not 2 base cases 
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,10):
    print(fib(i), ' ')
print('\n\n')
# THIS CODE IS INNFECIENT CAUSE IT CALLS ITSELF TWICE

# TO MAKE IT BETTER SEE IF YOU ALREADY CALCULATED THE VALUE FIRST
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans # POPULATE VALUE SO WE CAN USE IT LATER IF NEEDED
        return ans

d = {1:1, 2:2} # BASE CASES HERE
print(fib_efficient(6, d))
# note that this method only works for procedures without side effects
#   (i.e.,	the	procedure	will	always	produce	the	
#   same	result	for	a	specific	argument	independent	of	any	
#   other	computaSons	between	calls)