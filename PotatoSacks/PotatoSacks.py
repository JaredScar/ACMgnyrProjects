#
# Code property of Jared Scarito
#

testCases = int(input())
outCases = []
for i in range(testCases):
    weights = []
    dataSet = str(input())
    case = dataSet.split(" ")[0]
    maxWeight = int(dataSet.split(" ")[1])
    for weightIndex in range(len(dataSet.split(" "))):
        if int(weightIndex) > 1:
            weight = dataSet.split(" ")[int(weightIndex)]
            weights.append(int(weight))
    outCases.append("NO")
    sum = 0
    #sorted(weights, key=int)         #  Don't think it actually needs to be sorted...
    for weight in weights:
        sum += weight
        if sum > maxWeight:
            sum -= weight
        if sum == maxWeight:
            outCases[i] = "YES"
            break
        else:
            outCases[i] = "NO"
for caseNum in range(len(outCases)):
    print(str(caseNum + 1), str(outCases[caseNum]))
