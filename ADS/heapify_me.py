"""
A module for heap creation and handling
"""


def parent(i):
    i += 1
    p = i//2
    p -= 1
    return p


def left(i):
    i += 1
    p = 2*i
    p -= 1
    return p


def right(i):
    i += 1
    p = 2*i + 1
    p -= 1
    return p


def max_heapify(A, i):
    """
    Precondition: the subtrees of node i are max-heaps
    """
    # calculate indices of the children
    l = left(i)
    r = right(i)

    # establish who is the largest between parent, left child and right child, through comparisons
    if l <= heapsize-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize-1 and A[r] > A[largest]:
        largest = r

    # establish if the parent respects max-heap property or not; if not, bubble the largest child up
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # repeat: now that the parent has bubbled down, does it respect max-heap property in its new location?
        max_heapify(A, largest)


def build_max_heap(A):
    global heapsize
    heapsize = len(A)
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i)


def heapsort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 1, -1):  # i from length of A down to 2
        A[0], A[i] = A[i], A[0]
        global heapsize
        heapsize -= 1  # since heapsort depends on creation of a heap, the heapsize variable will always be defined
        max_heapify(A, 0)
    A[0], A[1] = A[1], A[0]  # swap the first two elements, which still respect max-heap property


if __name__ == "__main__":
    import random
    dummy = random.sample(range(1, 20), 10)
    # dummy = [2, 19, 9, 13, 1]
    print(dummy)
    heapsort(dummy)
    print(dummy)

# it would be very handy to define the heapsize as an attribute (i.e. define heaps as a class)
# global variables work quite well in this implementation, but they sound quite dicy to me
