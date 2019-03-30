def binary_search(A, v):
    # initialize indices
    p = 0
    r = len(A)

    while len(A[p:r]) > 1:
        q = (p+r)//2  # find midpoint

        # update right limit of search (r) if midpoint is greater than query
        if A[q] > v:
            r = q
        # update left limit of search (p) if midpoint is lesser than query
        elif A[q] < v:
            p = q
        # return current midpoint index if it's equal to query
        elif A[q] == v:
            return q

    # if we are out of the cycle, we have an array of length one.
    # either it's the element we're looking for, or it's not present in the array
    if A[p:r] == v:
        return p
    else:
        return None


if __name__ == "__main__":
    dummy = [1, 2, 3, 4, 5, 6, 8]
    query = 7
    res = binary_search(dummy, query)
    print(res)
