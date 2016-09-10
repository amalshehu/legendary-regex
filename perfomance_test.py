import time
import re

input = "maximum"

if "x" in input:
    print("Non-RE")

print time.clock()

if re.search("x", input):
    print("RE")

print time.clock()
