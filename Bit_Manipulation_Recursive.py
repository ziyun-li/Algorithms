# Given a exponentially large number, n, find the most efficient method reach 1, given that only 3 operations can be performed:
# 1) Add one
# 2) Remove one
# 3) Divide the entire group by 2

solution_list = {1:0,} #memoize n as key, number of solution as value
def solution_recursive(n):
    n = long(n)

    if n in solution_list:
        return solution_list[n]

    if n & 1: #if n is odd, take minimum of +1 or -1
        solution_list[n] = min(solution_recursive((n-1)>>1) + 2,solution_recursive((n+1)>>1) + 2)

    else: #if n is even, divide by 2
        solution_list[n] = solution_recursive(n >> 1) + 1

    return solution_list[n]
