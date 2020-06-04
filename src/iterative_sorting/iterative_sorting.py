# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i  # default smallest value
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # all the elements to the right of the default smallest
        for j in range(i+1, len(arr)):
            # if elements in j position is smaller
            if arr[j] < arr[smallest_index]:
                # change to smallest
                smallest_index = j

        # TO-DO: swap
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


print(selection_sort([3, 2, 4, 1, 5, 9, 8, 6, 7]))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        # inner loop over j from 0 to n - 1 - i -> last sorted element
        for j in range(0, len(arr)-1-i):
            # compare the current element to element to its right
            # if element on the left is greater than on the right
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([23, 12, 65, 32, 99, 66, 54]))

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
