import re

# Input string
value = "Tiny programs that process text."

match = re.search("(process.*)", value)
if match:
    print("Search result:", match.group(1))

match = re.match("(pr.*)", value)
if match:
    print("match:", match.group(1))
