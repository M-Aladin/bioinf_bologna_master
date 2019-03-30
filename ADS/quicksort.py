"""
QUICKSORT(A, p, r)
1. if p < r then
2. q ← PARTITION(A, p, r)
3. QUICKSORT (A, p, q-1)
4. QUICKSORT (A, q+1, r)


PARTITION (A, p, r)
1. x ← A[r]
2. i ← p – 1
3. for j=p to r-1 do
4. if A[j] ≤ x then
5. i ← i + 1
6. exchange A[i] ↔ A[j]
7. exchange A[i+1] ↔ A[r]
8. return i+1
"""


def partition(A, p, r):
    print(A[p:r])
    print(r)
    x = A[r]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


if __name__ == "__main__":
    dummy = [4, 5, 3, 7, 1]
    print(dummy)
    quicksort(dummy, 0, len(dummy))
    print(dummy)
