def m_inverse(A):
    # Create Augumented Matrix with identity matrix
    n = len(A)
    for j in range(len(A)):
        row = [0] * n
        row[j] = 1
        A[j] += row

    # Perform Row Operations on non-diagonal to set to 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and A[j][i] != 0:
                select_row = i
                multiplication_factor = A[j][i]/A[select_row][i]
                for n in range(2*len(A)):
                    A[j][n] = A[j][n] - (A[select_row][n]* multiplication_factor)

    # Perform Row Operations on diagonal to set to 1
    for i in range(len(A)):
        if A[i][i] != 1:
            multiplication_factor = A[i][i]
            for n in range(2*len(A)):
                A[i][n] = A[i][n]/multiplication_factor

    matrix_inverse = []
    for x in range(len(A)):
        matrix_inverse.append(A[x][int(len(A[0])/2):])

    return matrix_inverse
