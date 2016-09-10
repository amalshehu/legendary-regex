# Pattern details

# ^\d     Match at the start, check for single digit.
# .*\d$   Check for zero or more of any char.
#         Check for single digit.
#         Match at the end.


import re

list = ["123", "4dolphin", "crab5", "6shell"]
for item in list:

    # See if string starts in digit. (^)
    match = re.match("^\d", item)
    if match:
        print("START:", item)

    # See if string ends in digit. ($)

    match = re.match(".*\d$", item)
    if match:
        print("  END:", item)
