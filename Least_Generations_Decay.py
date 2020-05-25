
# Given 2 exponentially large numbers M and F, this program finds the least number of generations that needs to pass to obtain the given numbers M and F, given that we initially start from only 1 M and 1 F and they can increase in specific ways given by a set of rules below.
# Original question is taken from Google Challenge, in full below:

# _______________________________________________________________________
# You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.
#
# But there's a few catches. First, the bombs self-replicate via one of two distinct processes: Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created; Every Facula bomb spontaneously creates a Mach bomb.
#
# For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.
#
# Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good!
#
# And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)
#
# You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.

def solution(M,F):
    M, F = long(M), long(F)
    ans = 0

    # Keep repeating loop till M or F decays till 1
    while M > 1 or F > 1:
        # Impossible if either M or F equals 0, or M = F
        if M == F or M == 0 or F == 0:
            return "impossible"
            break
        # Find the larger of M or F. If M is larger, the previous "generation" values will have to be the M, the larger number subtracting the smaller value F.
        if M > F:
            count = long(M//F) if F > 1 else long(M//F) - 1
            # Reduces run time/ number of loops for extremely large numbers if M is much larger than F
            M = M % F
            ans += count
        # Else, vice versa.
        else:
            count = long(F//M) if M > 1 else long(F//M) - 1
            F = F % M
            ans += count

    return str(ans)

print(solution("11975","15567504"))
