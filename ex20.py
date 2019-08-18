# Function and Files
from sys import argv

script, inputFile = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(inputFile)

print("First let's print the whole file:\n")

print_all(current_file)

print("Let's rewind")

rewind(current_file)

print("Printing Lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)