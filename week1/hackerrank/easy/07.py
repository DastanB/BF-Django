def secondLowestGrade(classList):
    secondLowestScore = sorted(set(x[1] for x in classList))[1]
    result = sorted([x[0] for x in classList if x[1] == secondLowestScore])
    return result


numberOfStudents = int(input())
classList = []
for i in range(numberOfStudents):
    classList.append([str(input()), float(input())])
print('\n'.join(secondLowestGrade(classList)))