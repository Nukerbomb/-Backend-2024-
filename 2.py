A =  [2, 4, 1, 3, 2, 4, 6, 7, 9, 2, 19]
B = [2, 1, 4, 3, 6, 9]
C = []
for i in range(len(B)):
    for j in range(len(A)):
        if A[j]==B[i]:
            C.append(A[j])
A = sorted(A)
A = A[::-1]
for i in range(len(A)):
    if A[i] not in C:
        C.append(A[i])

A = C
print(A)