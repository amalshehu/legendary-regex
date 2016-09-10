import re

phonebook = open("phonebook.txt")
for line in phonebook:
    if re.search(r"J.*Neu",line):
        print line.rstrip()
phonebook.close()

