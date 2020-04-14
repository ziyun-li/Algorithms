from __future__ import division

# isclose function of math module, built in for python 3.5 onwards
def isclose(a, b, rel_tol=1e-15, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def convert_probability_to_fraction(l):
    minimum = min(i for i in l if i >0)
    fraction_list = []
    multiple_list = []

    for i in l:
        if i != 0:
            multiple_of_minimum = i/minimum
            fraction_list.append(multiple_of_minimum)
            multiple = 1
            while isclose(multiple_of_minimum,round(multiple_of_minimum)) == False:
                multiple += 1
                multiple_of_minimum += i/minimum
            multiple_list.append(multiple)
        else:
            fraction_list.append(0)
            multiple_list.append(0)

    for i in range(len(fraction_list)):
        fraction_list[i] = int(round(max(multiple_list) * fraction_list[i]))
    fraction_list.append(sum(fraction_list))

    return fraction_list


# Matrix Inverse
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


# Matrix Multiplication
def m_mult(A,B):
    result = []
    for i in range(len(A)): # iterate through rows of A
        row = [0]*len(B[0])
        result.append(row)
        for j in range(len(B[0])): # iterate through columns of B
            for k in range(len(B)): # iterate through rows of B
                result[i][j] += A[i][k] * B[k][j]
    return result


def solution(m):
    if len(m) == 1:
        Ans = [1,1]
    else:
        unstable_state = [0,]
        terminal_state = []
        matrix_size = len(m)
        for i in range(1,matrix_size):
            if sum(m[i]) == 0:
                terminal_state.append(i)
            else:
                unstable_state.append(i)

        # transform count to probability
        for x in unstable_state:
            total = sum(m[x])
            for y in range(matrix_size):
                m[x][y] = m[x][y]/total

        R = []
        Q = []
        for x in unstable_state:
            R_list = []
            for y in terminal_state:
                R_list.append(m[x][y])
            R.append(R_list)
            Q_list = []
            for z in unstable_state:
                Q_list.append(m[x][z])
            Q.append(Q_list)

        transition_matrix = []
        for j in range(len(Q)):
            row = [0]*len(Q)
            row[j] = 1
            transition_matrix.append(row)
        for i in range(len(Q)):
            for j in range(len(Q)):
                transition_matrix[i][j] = transition_matrix[i][j] - Q[i][j]

        F = m_inverse(transition_matrix)
        RF = m_mult(F,R)
        Ans = convert_probability_to_fraction(RF[0])

    return Ans
