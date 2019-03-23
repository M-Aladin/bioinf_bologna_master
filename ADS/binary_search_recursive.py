"""
Binary search algo -- recursive:
given an ordered list, compare the midpoint with the query
divide the list in half and discard the half that for sure doesn't contain the query
keep dividing until the result is found.

BINARY SEARCH(A,v,p,r):
    q = (p+r)//2
    if A[q] > v then
        binary search(A, v, p, q)
    elif A[q] < v then
        binary search(A, v, q, r)
    else
        return q
"""


def binary_search(A, v, p, r):
    print(A[p:r])
    q = (p+r) // 2
    if A[q] > v and len(A[p:r]) > 1:
        return binary_search(A, v, p, q)
    elif A[q] < v and len(A[p:r]) > 1:
        return binary_search(A, v, q, r)
    elif A[q] == v:
        return q
    else:
        return None  # this value raises a TypeError when we print the output in test code


if __name__ == "__main__":
    dummy = [1, 2, 3, 4, 5, 7]
    query = 6
    res = binary_search(dummy, query, 0, len(dummy))
    print(dummy)
    try:
        print("The query %d is found in position %d" % (query, res))
    except TypeError:
        print("The query %d is not in the array" % query)
