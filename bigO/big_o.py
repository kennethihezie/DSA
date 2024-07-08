# Big O: is the lanaguage and metric we use to describe the efficiency of algorithms
# Time Complexity: A way of showing how the runtime of a function increases as the size of input increases.
# Space Complexity: The amount of memory that some code used to run.
# Best case, Average case and Worst case

# Runtime Complexities
# O(1) === Constant === A simple add numbers function
# O(n) === Linear === Loop through numbers from 1 to n
# O(LogN) === Logarithmic === Find an element in sorted array
# O(n^2) === Quadratic === Nested loops
# O(2^N), also known as exponential time complexity, describes an algorithm where the time it takes 
# to complete the task doubles with each additional input element. This often happens in algorithms 
# that solve problems by generating all possible combinations or subsets, such as the recursive 
# solution for the Fibonacci sequence or the subset-sum problem.


# O(1) example:
def o_1(n):
    return n * n

# O(n) example
def o_n(n):
    for i in range(n):
        print(i)


# drop constants
# O(2N) == O(N) 
def o_n_another_example(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)


# O(LogN) example
# Refer to divider and conquer.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found


# O(n^2)
def o_n_2(n):
    for i in range(n):
        for j in range(n):
            print(i)

# O(2^n)
def o_2_n(n):
    for i in range(n):
        for j in range(n):
            print(i)
    
    for k in range(n):
        print(k)


# Space complexity
def space_complexity(n):
    if n <= 0:
        return 0
    return n + sum(n -1)


# Complex cases:
# The runtime complexity of the below functions will be
# O(a + b)
# If your algorithm is in this form do this, then when you are all done, do that, then add the runtimes
def complex_one(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)


# Complex cases:
# The runtime complexity of the below functions will be
# O(a * b)
# If your algorithm is in this form do this, then when you are all done, do that, then multiply the runtimes
def complex_two(a, b):
    for i in range(a):
        for j in range(b): 
           print(i, j) 
    


# measuring code using bigO
def findBiggestNumber(arr): 
    biggestNumber = arr[0]  # =====================> O(1)
    for i in range(1, len(arr)):   # ==============> O(n)
        if arr[i] > biggestNumber:  # =============> O(1)
            biggestNumber = arr[i]  # =============> O(1)

    print(biggestNumber)   # ======================> O(1)


# Solution
# Sum line 85 and 86 which is O(1) + O(1) = O(2) remember droping constants so which is == O(1)
# Sum the result of line 85 and 86 which is O(1) + line 88 which is O(1) == O(1) remember droping constants.
# Sum the result O(1) + line 83 which is O(1) == O(1) remember droping constants.
# finally sum line 84 which is O(n) + O(1) = O(n)  remember droping non dominat terms for pre-dominat terms
# result = O(n)

# What does it mean when we say that an algorithm X is asymptotically more efficient than Y? 
# X will always be a better choice for large inputs.