"""
Assumption for counting sort: elements to be sorted are in a range from 0 to k, where k << n
"""


def counting_sort(A, B, k):
    """
    Disclaimer: not proper documentation, just me wondering
    It's just so strange to have the output array passed as a parameter and modified in place
    """
    # initialize counters
    C = [0 for i in range(k)]

    # count repetitions in input array
    for i in range(len(A)):
        C[A[i]] += 1

    # make counting array cumulative
    for i in range(1, k):
        C[i] += C[i-1]

    for j in range(len(A)-1, -1, -1):  # j goes from greatest index of A down to 0
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]-1]


if __name__ == "__main__":
    import random
    k = 4
    dummy = [random.randint(0, 3) for i in range(10)]
    print(dummy)
    output = [0 for i in range(len(dummy))]
    counting_sort(dummy, output, k)
    print(dummy)