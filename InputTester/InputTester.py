#
# Code property of Jared Scarito
#
import subprocess
import requests
import io

# Test Judge Input:
# http://acmgnyr.org/year2018/data/a.in
# Test Judge Output:
# http://acmgnyr.org/year2018/data/a.out
websiteHTML = requests.get(input("What is the Judge's input tests URL? \n").replace(" ", "")).text
outHTML = requests.get(input("What is the Judge's output tests URL? \n").replace(" ", "")).text.split("\n")
inputs = websiteHTML.split("\n")

pythonFile = input("What is the Python File that you want to test the judge's input tests against? \n (Must be in same directory as this file) \n")
child = subprocess.Popen('python ' + pythonFile, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
for i in range(len(inputs)):
    if(len(inputs) > 0):
        child.stdin.write(inputs[i].encode())
        child.stdin.flush()
child.stdin.close()
cout = 0
for line in io.TextIOWrapper(child.stdout, encoding="utf-8"):
    checkedLine = line.replace("\n", "")
    if(outHTML[cout].strip() != checkedLine.strip()):
        print(str(cout) + " YOUR ANSWER: " + checkedLine + " --- " + "RIGHT ANSWER: " + str(outHTML[cout]))
        print(str(cout) + " INPUT: " + str(inputs[cout]).replace(str(cout), ""))
    else:
        print(checkedLine)
    cout += 1
child.terminate()