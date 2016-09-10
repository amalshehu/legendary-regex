import time
import re
print("############### TEST 1 ################")
input = "maximum"

if "x" in input:
    print("Non-RE")

t1 = time.clock()
print (t1)

if re.search("x", input):
    print("RE")

t2 = time.clock()
print(t2)

if(t1 < t2):
    print "Non-RE is faster."
else:
    print ("RE is faster.")
