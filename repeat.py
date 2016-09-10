import re

values = ["gold100", "---200", "xxxyyy", "jjj", "points4000", "skills500"]
for item in values:

    # Require 3 letters OR 3 dashes.
    # ... Also require 3 digits.
    match = re.match("(?:(?:\w{4})|(?:\-{3}))\d\d\d$", item)
    if match:
        print("  OK:", item)
    else:
        print("FAIL:", item)
