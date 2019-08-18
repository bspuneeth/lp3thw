# Copying files

from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print(f"Copying files from {fromFile} to {toFile}")
inFile = open(fromFile)
inData = inFile.read()

print(f"The input file is {len(inData)} bytes long")
print(f"Does the output file exists? {toFile} ")
print('Hit RETURN to continue or CTRL+C to abort. ')

input()

outFile = open(toFile, 'w')
outFile.write(inData)

print("Job Done")

outFile.close()
inFile.close()