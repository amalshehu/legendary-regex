import re
# Lets use a regular expression to match a date string.
# We are just testing if the regex matches.
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "September 9"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string
    # If we want, we can use the MatchObject's start() and end() methods
    # to retrieve where the pattern matches in the input string, and the
    # group() method to get all the matches and captured groups.
    match = re.search(regex, "September 9")
    print "Match at index %s, %s" % (match.start(), match.end())
    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1) match.group(2), ... will return the capture
    #    groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)

    print "Full match: %s" % (match.group(0))# So this will print "September 9"
    print "Month: %s" % (match.group(1))  # So this will print "September"
