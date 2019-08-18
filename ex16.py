# Reading and Writing Files

from sys import argv

script, fileName = argv

print(f"We are going to erase file name {fileName}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(fileName, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Enter 3 lines below:")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Writing these files to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"Closing {fileName}. Good Bye !!")
target.close()
