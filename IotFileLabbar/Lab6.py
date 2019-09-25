import os


path = input("Ange path->")
fil = input("Ange del av filnamn att söka efter->")

for f in os.listdir(path):
    if f.upper().find(fil.upper()) != -1:
        fullPath = os.path.join(path,f)
        print(f"{f} - bytes = {os.path.getsize(fullPath)} ")
            