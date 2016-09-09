import re
# Lets try and reverse the order of the day and month in a date
# string. Notice how the replacement string also contains metacharacters
# (the back references to the captured groups) so we use a raw
# string for that as well.
regex = r"([a-zA-Z]+) (\d+)"

# This will reorder the string and print:
#   16 of July, 09 of September, 12 of December
print re.sub(regex, r"\2 of \1", "July 16, September 09, December 12")
