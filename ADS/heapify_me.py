"""
A module for heap creation and handling
"""


def parent(i):
    i += 1
    p = 2*i
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


def max_heapify(A,i):
    """
    Precondition: the subtrees of node i are max-heaps
    :param A:
    :param i:
    :return:
    """
    l = left(i)
    r = right(i)
    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


