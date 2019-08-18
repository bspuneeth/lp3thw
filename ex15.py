# Reading Files


from sys import argv

script, filename = argv

text = open(filename)

print(f"Here's your file {filename}")
print(text.read())


print("Type the file name again:")
fileagain = input("> ")

textAgain = open(fileagain)
print(textAgain.read())
