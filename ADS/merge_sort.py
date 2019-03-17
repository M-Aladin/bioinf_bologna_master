"""
MERGE-SORT(A, p, r):
if p<r then
    q <- (p+r)/2
    merge-sort(A, p, q)
    merge-sort(A, q+1, r)
merge(A, p, q, r)

MERGE(A, p, q, r):
n1, n2 <- length[p-q], length[q+1-r]
L <- A[1... n1] + [infinite]
R <- A[n1+1... A.length] + [infinite]
i <- 1, j <- 1
for k <- p to r, do:
    if L[i] <= R[i]
        then A[k] <- L[i]
        i <- i+1
    else
        A[k] <- R[j]
        j <- j+1
"""

from math import inf


def merge_sort(A, p, r):
    if p+1 < r:
        # divide
        q = (p+r)//2
#        print(A[p:q], A[q:r])
        # conquer
        merge_sort(A, p, q)
        merge_sort(A, q, r)

        # combine
        merge(A, p, q, r)
#        print(A[p:r])


def merge(A, p, q, r):
    # n1 = q - p
    # n2 = r - q

    # temp arrays
    left = A[p:q] + [inf]
    right = A[q:r] + [inf]

    i, j = 0, 0

    for k in range(p, r):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


if __name__ == "__main__":
    dummy = [64, 82, 53, 27, 41, 98]
    # kudos to my flatmate for the dummy list
    print(dummy)
    merge_sort(dummy, 0, len(dummy))
    print(dummy)
