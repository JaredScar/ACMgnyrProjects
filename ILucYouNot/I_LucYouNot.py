#
# Code property of Jared Scarito
#
def getLucasSeq(length):
    lucSeq = ["2", "1"]
    n = 0
    if(length > 1):
        while n !=length:
            if n > 1:
                lastLast = int(lucSeq[(n - 2)])
                last = int(lucSeq[(n - 1)])
                lucSeq.append(str(lastLast + last))
            n += 1
    else:
        return ["2"]
    return lucSeq

testCases = int(input("How many test cases will there be?: \n"))

lengths = []
for num in range(testCases):
    print(str(num + 1), end=" ")
    lengths.append(int(input()))
num = 0
while num < len(lengths):
    print(" ".join(getLucasSeq(lengths[num])))
    num += 1
