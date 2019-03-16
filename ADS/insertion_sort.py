"""
Insertion-sort algorithm

INSERTION-SORT(A):
1. for j <- 2 to A.length do:
2.     key <- A[j]
3.     i <- j-1
4.     while i > 0 and A[i] > key do:
5.         A[i+1] <- A[i]
6.         i <- i-1
7.     A[i+1] <- key
"""


def ins_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


if __name__ == "__main__":
    ex = [5, 2, 4, 6, 1, 3]
    print(ins_sort(ex))
