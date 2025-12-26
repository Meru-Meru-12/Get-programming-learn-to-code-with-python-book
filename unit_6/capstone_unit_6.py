# The problem
# You're given two files containing text. Using the names of the files, write a program that reads the documents and uses a metric to determine how similar they are.
# Documents that are exactly the same should get a score of 1, and documents that don't have any words in common should get a score of 0.

def read_text(filename):
    inFile =  open(filename, 'r')
    line = inFile.read()
    return line

text =  read_text("sonnet18.txt")
print(text)

print(read_text("sonnet18.txt"))
