import os
def swapFileData():
    File1 = input("Input file 1 name: ")
    File2 = input("Input file 2 name: ")

    os.rename(File2, 'temp')
    os.rename(File1, File2)
    os.rename('temp', File1)
    print("!! Successfully Done From", File1, "To", File2, "!!")
swapFileData()