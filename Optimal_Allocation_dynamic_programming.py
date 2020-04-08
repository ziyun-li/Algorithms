def solution(total_credit):
    """
    This algorithm allocates credits to workers(minions).
    However it must follow a set of rules. (inspired by Google challenge)
    1) The most junior minion (with the least seniority) gets exactly 1 credit.
    2) A minion will revolt if the person who ranks immediately above them gets more than double the number of credits they do.
    3) A minion will revolt if the amount of credits given to their next two subordinates combined is more than the number of credits they get.
    4) You can always find more minions to pay

    This function finds an integer which represents the difference between the minimum and maximum number of minions who can share the credits.
    """

#calculate generous strategy
    generous_list =[1]
    generous_credit = 1
    generous_minion_count = 1
    generous_creditleft = total_credit - 1
    while generous_creditleft >= generous_list[-1]*2:
        generous_credit = generous_list[-1]*2
        generous_list.append(generous_credit)
        generous_creditleft -= generous_credit
        generous_minion_count += 1

#calculate stingy strategy
    stingy_minion_count = 1
    if total_credit > 1:
        stingy_list = [1,1]
        stingy_minion_count = 2
        stingy_creditleft = total_credit - 2
        while stingy_creditleft >= stingy_list[stingy_minion_count-2] + stingy_list[stingy_minion_count-1]:
            stingy_credit = stingy_list[stingy_minion_count-2] + stingy_list[stingy_minion_count-1]
            stingy_list.append(stingy_credit)
            stingy_minion_count += 1
            stingy_creditleft -= stingy_credit

    return  stingy_minion_count - generous_minion_count

total_credit= 143

print(solution(total_credit))
