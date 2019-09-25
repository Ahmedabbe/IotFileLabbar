import os

lines = []
with open("SampleFile-Lab4Result.txt", "w") as outDataFile:
    with open("Lab5TextFile-InData1.txt", "r") as indataFile1:
        lines = indataFile1.readlines()
        lines = sorted(lines, key=str.lower)
        outDataFile.writelines(lines)

