#
# Code property of Jared Scarito
#
def getTheMeans(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return "{:.3f}".format(float(sum)/float(len(numbers)))
numbers = []
answers = []
testCases = int(input("How many test cases do you want? \n"))
for i in range(testCases):
    print(str(i + 1), end=" ")
    for i in range(int(input())):
        numbers.append(int(input()))
    answers.append(getTheMeans(numbers))
for i in range(testCases):
    print(answers[i])
