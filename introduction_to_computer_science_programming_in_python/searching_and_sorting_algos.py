# searching is finding an item or group of items with specific properties within a collection of items
#   IMPLICIT COLLECTION: like find square root as a search problem, exhaustive enumeration, bisection search, Newton-Raphson
#   EXPLICIT COLLECTION: like is a student record in a stored database

# LINEAR SEARCH (BRUTE FORCE AKA BRISITH MUSEUM ALGORITHM) O(n)
#   unsorted list version O(n)
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True # you can speed up a bit by returning true here but it doesn't impact worst case (searching through whole list)
        return found
    return found
#   sorted list version O(n)
#   must only look until reach a number greater than e
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# BISECTION SEARCH
#   LIST MUST BE SORTED to monotomic to give correct answer
#   remember can avoid passing list to function calls to avoid a part with O(n) complexity
#   overall complexity of O(log(n)) size reduces by factor of 2 on each step, list never copied repassed as pointer
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
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
# DOES IT EVER MAKE SENSE TO SORT FIRST THEN SEARCH? NO!
#   SORT+O(log(n))<O(n) -> SORT<O(n)–O(log(n))
#   makes sense when sorting is less than O(n) which is never true since to sort you need to look at every element at least once

# SO WHY BOTHER SORTING FIRST? YOU MAY SORT ONCE AND THEN DO MANY SEARCHES
#   YOU CAN SEE THIS IF YOU AMORTIZE COST OF THE SORT OVER MANY SEARCHES
#   SORT+K*O(log n)<K*O(n) FOR LARGE K SORT TIME BECOMES IRRELEVANT, cost of sorting is small enough

# BUBBLE SORT
# run through list over and over again, comparing consecutive pairs, swap if out of order, break if no swaps in a run though list
# O(n)*O(n) cause two loops complexity SO O(n^2) complexity
def bubble_sort(L):
    swap = False # to keep track of when there are no more swaps
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)

# SELECTION SORT
# extract minimum element first, swap it with element at index 0
# next step extract 2nd least element, swap it with element at index 1
# go on and on
# so at ith step, first i elements of list are sorted
# O(n^2) complexity
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L): # iterates of list indexes O(n) worst case
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)): # iterates of list indexes O(n) worst case but actually like O(n-i)
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 
testList = [1,3,5,7,2,6,25,18,13]
       
print('')
print(selection_sort(testList))
print(testList)

# MERGE SORT
#   using divide-and-conquer approach
#       1. if list is len 0 or 1 it's already sorted
#       2. if list has more than one element, split and sort each list
#       3. merge sorted sublists at the end by comparing elements and moving smaller element to result
#       4. when one list is empty just copy rest of other list
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right): # O(n) where o is length of shorter list
        if left[i] < right[j]: # order the result by iterating through ordered lists
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)): # when right sublist is empty O(n)
        result.append(left[i])
        i += 1
    while (j < len(right)): # when left sublist is empty O(n)
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right) # O(nlog(n)) by dividing list in half with each recursion call
# OVERALL COMPLEXITY IS O(nlog(n)) where n is len(L)
# This is the fastest a sort can be
testList = [1,3,5,7,2,6,25,18,13]

print('')
print(merge_sort(testList))

# MOST IMPORTANT PART OF COMPUTATIONAL THINKING (THE 3 A'S)
#   1. CHOOSING THE RIGHT ABSTRACTIONS WITH RELATIONSHIPS BETWEEN THEM (LIKE CLASSES PARENT/CHILD)
#   2. AUTOMATION 
#   3. ALGORITHMS

# REMEMBER TO THINK RECURSIVELY, REFORMULATING A DIFFICULT PROBLEM INTO ONE WHICH WE KNOW HOW TO SOLVE
#   REDUCTION, EMBEDDING, TRANSFORMATION, SIMULATION

