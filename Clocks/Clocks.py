#
# Code property of Jared Scarito
#
def solve(clocks, offsets):
    solvedTime = None
    for i in range(len(clocks)):
        clock1 = clocks[i]
        time1 = None
        for offsetIndex in range(len(offsets)):
            offset1 = offsets[offsetIndex]
            if (str(offset1[0]) == '-'):
                time1 = addTimes(time1, offset1.split("-")[1])
            else:
                time1 = subTime(time1, offset1)
            for j in range(len(clocks)):
                clock2 = clocks[j]
                for offsetIndex2 in range(len(offsets)):
                    offset2 = offsets[offsetIndex2]
                    if (str(offset2[0]) == '-'):
                        time2 = addTimes(time2, offset2.split("-")[1])
                    else:
                        time2 = subTime(time2, offset2)
                    if (time1 == time2 and solvedTime != None and time1 != solvedTime):
                        return None
                    if (time1 == time2):
                        solvedTime = time1
    return solvedTime


def addTimes(time1, time2):
    # 4:30 + 9:40
    # 0123   0123
    time1Hour = time1.split(":")[0]  # 4
    time2Hour = time2.split(":")[0]  # 9

    time1Mins = time1.split(":")[1]  # 30
    time2Mins = time2.split(":")[1]  # 40

    time1min1 = int(time1Mins[0])  # 3
    time1min2 = int(time1Mins[1])  # 0
    time2min1 = int(time2Mins[0])  # 4
    time2min2 = int(time2Mins[1])  # 0

    min2Total = time1min2 + time2min2
    add1ToMin1 = 0
    if (min2Total >= 10):
        min2Total = int(str(min2Total)[1])
        add1ToMin1 = 1
    min1Total = time1min1 + time2min1 + add1ToMin1
    add1ToHour = 0
    if (min1Total >= 10):
        min1Total = int(str(min1Total)[1])
        add1ToHour = 1
    hourTotal = time1Hour + time2Hour + add1ToHour
    if (hourTotal > 12):
        hourTotal -= 12
    return str(hourTotal) + ":" + str(min1Total) + str(min2Total)


def subTime(time, timeSubtracted):
    # 12:00 - 3:30
    # 01234   0123
    time1Hour = int(time1.split(":")[0])  # 12
    time2Hour = int(time2.split(":")[0])  # 3

    time1Mins = time1.split(":")[1]  # 00
    time2Mins = time2.split(":")[1]  # 30

    time1min1 = int(time1Mins[0])  # 0
    time1min2 = int(time1Mins[1])  # 0
    time2min1 = int(time2Mins[0])  # 3
    time2min2 = int(time2Mins[1])  # 0

    min2Total = time1Min2 - time2Min2


outCases = []
testCases = int(input())  # How many test cases they want?
for i in range(testCases):
    numClocksAndOffsets = int(input())  # How many clocks (with times and labels)?
    clocks = []
    offsets = []
    for j in range(numClocksAndOffsets):
        clocks.append(str(input()))  # What is the time on the clock?
    for j in range(numClocksAndOffsets):
        offsets.append(str(input()))  # What is the offset label saying?
    solved = solve(clocks, offsets)
    if (solved != None):
        outCases[i] = solved
    else:
        outCases[i] = i
for caseIndex in range(len(outCases)):
    print(str(caseIndex + 1), str(outCases[i]))