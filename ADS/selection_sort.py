"""
SELECTION SORT(A):
for i <- 1 to A.length-1 do:
    min = infinite
    for j <- i to n do:
        if A[j] < min then
            min <- A[j]
            counter <- j
    A[counter] <- A[i]
    A[i] <- min


Pseudocode from Wikipedia (not implemented here):
procedure SelectionSort(a);
  for i = 0 to n - 1
    posmin ← i
    for j = (i + 1) to n
      if a[j] < a[posmin]
        posmin ← j
    if posmin != i
        tmp ← a[i]
        a[i] ← a[posmin]
        a[posmin] ← tmp
"""
from math import inf


def sel_sort(array):
    for i in range(len(array)-1):  # traverse the array until 2nd-to-last position

        mini = inf
        # counter = i  # if the lowest value is at the 1st position of sub-array, the counter is never reassigned
        # # so I need to initialize the variable
        # (((edit: it's not necessary to initialize, as any number in the array will be < infinity)))

        for j in range(i, len(array)):  # traverse the sub-array that goes from current position to end
            if array[j] < mini:
                # if the conditions are met, update the temporary variables
                mini = array[j]
                counter = j
        # exchange the values of the two positions in the array
        array[counter] = array[i]
        array[i] = mini


if __name__ == "__main__":
    dummy = [9, 13, 7, 1, 2, 0, 10, 20]
    print("Unsorted list:\n", dummy)
    sel_sort(dummy)
    print("Sorted list:\n", dummy)
