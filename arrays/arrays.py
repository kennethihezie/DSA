import array as arr
import numpy as np

# using numpy
empty_numpy_array = np.array([], dtype=int)   # Time complexity of empty numpy array module is O(1) constant time and Space complexity is O(1) 
numpy_array = np.array([1, 2, 3, 4], dtype=int)    # Time complexity of creating array with elemnt in it is O(N) linear time and Space complexity is O(N)



# using python array module
empty_array = arr.array('i')   # Time complexity of empty array module is O(1) constant time and Space complexity is O(1)
my_array = arr.array('i', [1, 2, 3, 4])   # Time complexity of creating array with elemnt in it is O(N) linear time and Space complexity is O(N)


def insert_element(array: arr.array, element, index: int):
    '''
    Time complexity of inserting an element depends on the number of element shift backwards which is O(N) linear time and Space complexity is O(1)
    Time complexity of the insert_element will vary. If you insert an element in the first or middle the time complexity is O(N), but if you insert at the end it will be O(1).
    Space time complexity is O(1) because we don't need an extra location to perform the operation.
    '''
    return array.insert(index, element)

# print(insert_element(my_array, 5, 2))


def transver_array(array: arr.array):
    '''
    Time complexity of the transver_array is O(N) remeber droping non-dominat terms for dominat terms.
    Space time complexity is O(1) because we don't need an extra location to perform the operation.
    '''
    for i in array:    # Time complexity is O(N)
        print(i)       # Time complexity is O(1)

# print(transver_array(my_array))

def access_element_array(array: arr.array, index: int):
    '''
    Time complexity of the access_element_array is O(1) remeber droping constants.
    Space time complexity is O(1) because we don't need an extra location to perform the operation.
    '''
    if(index >= len(array)):    #  Time complexity is O(1)
        print('There is not any element in this index')   #  Time complexity is O(1)
        return
    else:
        print(array[index])  #  Time complexity is O(1)

# print(access_element_array(my_array, 2))


def linear_search(array: arr.array, target):
    '''
    Time complexity of the linear_search is O(N) remeber droping non-dominat terms for dominat terms.
    Space time complexity is O(1) because we don't need an extra location to perform the operation.
    '''
    for i in range(len(array)):   # Time complexity is O(N)
        if array[i] == target:    # Time complexity is O(1)
            return i              # # Time complexity is O(1)
        
    return -1                     # Time complexity is O(1)

# print(linear_search(my_array, 4))


def remove_element(array: arr.array, element):
    '''
    Time complexity of the remove_element will vary. If you remove the first or middle element the time complexity is O(N), but if you remove the last element it will be O(1).
    Space time complexity is O(1) because we don't need an extra location to perform the operation.
    '''
    return array.remove(element)


# print(remove_element(my_array, 3))











