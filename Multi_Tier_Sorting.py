

def solution(l):
    """
    We can use existing algorithms to sort numbers. However, how can we sort released "versions".
    When there is a new release, major numbers are updated. e.g. 1,2,3 When new features are added to an software without being a complete new version, a second number named "minor" can be used to represent those new additions. e.g. 1.0,1.1,1.2. Small revisions and maintenance work are added to revision, e.g. 1.1.1,1.1.2
    This algorithm takes a list of versions and sorts them accordingly based on major, minor and revisions.

    Example input: l = ["1.1.2","98.12.6","1.0", "1.3.3","3.0" "1.1000.12","3.0.5", "1.0.12"]
    Example output: ["1.0", "1.0.12", "1.1.2", "1.3.3", "1.1000.12","3.0","3.0.5","98.12.6"]

    """
    for i in range(len(l)):
        l[i]=l[i].split('.')

    #groups all majors
    major_list = {}
    for x in range(len(l)):
        major_number = int(l[x][0])
        if major_number not in major_list:
            major_list[major_number] = [l[x]]
        else:
            major_list[major_number].append(l[x])

    #groups all minors and sorts revisions within each minor
    for key,value in major_list.items():
        minor_list = {}
        for y in range(len(value)):
            minor_number = int(value[y][1])+1 if len(value[y]) != 1 else 0
            if minor_number not in minor_list:
                minor_list[minor_number] = [value[y]]
            elif minor_number == 0:
                minor_list[minor_number].append(value[y])
            else:
                try:
                    ordered_revision_list = minor_list[minor_number]
                    position = len(ordered_revision_list)
                    for j in range(len(ordered_revision_list)):
                        if len(ordered_revision_list[j]) == 2:
                            continue
                        elif int(value[y][2]) < int(ordered_revision_list[j][2]):
                            position = j
                            break
                    ordered_revision_list.insert(position,value[y])
                    minor_list[minor_number] =  ordered_revision_list
                except:
                    if len(value[y]) == 2:
                        minor_list[minor_number].insert(0,value[y])
            major_list[key] = minor_list


    answer =[]
    for major in sorted(major_list.keys()):
        if type(major_list[major]) == list:
            answer += (minor_list)
        else:
            for minor in sorted(major_list[major].keys()):
                answer += major_list[major][minor]

    for n in range(len(answer)):
        answer[n] = '.'.join(answer[n])
    return answer



l=["1.1.2", "1.1.2", "1.0", "12.3.0", "1.48.20", "1.3.3", "1.0.12", "1.0.2", "2.0.0", "2.0", "2.0.12", "2.3.1", "2.0.2", "2.0.12","0","0.1","0.1.0","0.1.1","1.0","1","1.1.1","1.1.2","0.0","1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2","1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0","0.0","0","4.3.5","4.3.2","100.4.5","100.4.3","19.4.3","108.4.3","170.4.3","1000.4.3","1000.990.3","1000.101.3","1.1.2", "1.1.2", "1.0", "12.3.0", "1.48.20", "1.3.3", "1.0.12", "1.0.2", "2.0.0", "2.0", "2.0.12", "2.3.1", "2.0.2", "2.0.12","0","0.1","0.1.0","0.1.1","1.0","1","1.1.1","1.1.2","0.0","1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2","1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0","0.0","0","4.3.5","4.3.2","100.4.5","100.4.3","19.4.3","108.4.3","170.4.3","1000.4.3","1000.990.3","1000.101.3"]

print(len(l))
import time
start_time = time.time()
print(solution(l))
print("\nThis took %s seconds." % (time.time() - start_time))
