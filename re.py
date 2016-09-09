import re
# Lets use a regular expression to match a date string.
# We are just testing if the regex matches.
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "September 9"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string
