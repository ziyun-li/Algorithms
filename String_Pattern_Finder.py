def solution(s):
    """
    This function takes in a string s, and finds the maximum equal splits of s
    Example, s = abcabcabcab, pattern = abc, max_eqal_split = 3
    s = aaaaaaaaaaaaaaabbbbbbaaaaaaaaaaaaaaabbbbbb, pattern = aaaaaaaaaaaaaaabbbbbb, max_equal_split = 2

    """
    #collect index positions of first unique letter of the pattern
    first_letter_position=[]
    #collect index positions of second unique letter of the pattern
    second_letter_position=[]
    #for loop iterates through each index in the string to find the index positions of the first unique letter and the second unique letter
    for i in range(len(s)):
        if s[i]==s[0]:
            first_letter_position.append(i)
        #adds second unique letter that occurs in string. Ignores any subsequent 3rd to nth unique letters.
        elif len(second_letter_position) == 0:
            second_letter_position.append(i)
        else:
            #collect all positions of the second unique letter, only if it is after an occurence of the first letter letter
            #Rationale: if first unique letter has not occurred again, pattern has NOT repeated
            lapsed_indexes_from_last = range(second_letter_position[-1],i)
            if set(lapsed_indexes_from_last)-set(first_letter_position)!=set(lapsed_indexes_from_last):
                if s[i] == s[second_letter_position[0]]:
                    second_letter_position.append(i)

    # if second_letter_position is empty, there is only 1 unique letter in the entire string. The entire string will be a repetition of the first letter that appears.
    if len(second_letter_position) ==0:
        max_equal_part=len(s)
    # if  len(second_letter_position) is at least 2, and the second unique letter only occurs once in the pattern, the pattern will repeat at least 2 times. The exception is if the pattern consists of multiple first and second letter positions, e.g. abaaaab, and this is handled using "except"
    elif len(second_letter_position) >=2:
        try:
            n=1
            #length of pattern is given by difference in position of one of the second letter positions.
            len_pattern = second_letter_position[n] - second_letter_position[0]
            #We iterate through the indexes to handle exception cases where second letter position occurs more than once in a single pattern.
            while True:
                if s[:len_pattern] == s[len_pattern:len_pattern+len_pattern]:
                    break
                else:
                    n+=1
                    len_pattern = second_letter_position[n] - second_letter_position[0]
            max_equal_part=len(s)/len_pattern
        #Indexerror indicates all positions in second_letter_position has been input into while loop but no match in pattern is found. This means that all positions in second_letter_position are within the same pattern, the pattern does not repeat.
        except IndexError:
            max_equal_part=1
    # If  len(second_letter_position) == 1, the second unique letter only appears once. The pattern does not repeat.
    else:
        max_equal_part=1
    return max_equal_part
