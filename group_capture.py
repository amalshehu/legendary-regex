import re
# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "July 16, September 09, December 12")
for match in matches:
    # This will print:
    #   July 16
    #   September 09
    #   December 12
    print "Full match: %s" % (match)
# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "July 16, September 09, December 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print "Match month: %s" % (match)
