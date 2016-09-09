import re
# Lets create a pattern and extract some information with it
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the standard")
if result:
    # This will print:
    #   0 11
    # for the start and end of the match
    print result.start(), result.end()
# This will print:
#   Hello
#   Crazy
# for each of the captured groups that matched
for result in regex.findall("Hello World, Crazy World"):
    print result
