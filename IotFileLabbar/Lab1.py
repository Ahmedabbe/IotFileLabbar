import os

odd = True
with open("SampleFile-Lab1.txt","r") as f:
    for line in f:
        if odd:
            print(line.strip())
        if odd == True:
            odd = False
        else:
            odd = True
        #odd = not odd

#print(os.getcwd())
#OBS strip
