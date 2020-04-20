
# Given a exponentially large number, n, find the most efficient method reach 1, given that only 3 operations can be performed:
# 1) Add one
# 2) Remove one
# 3) Divide the entire group by 2

def solution(n):

    n = long(n)
    steps = 0
    THRESHOLD = 3

    while n > 1:
        if not (n & 1): #if even
            n = n >> 1
        else: #if odd
            n = n + 1 if (n&THRESHOLD == THRESHOLD and n != THRESHOLD) else n - 1
        steps += 1

    return steps


A ='9348304820948290482903489248392483209482948230948239482309489234829482394829480258908534053490593593405930593053945849583495839589358395938539'

print(solution(A))
