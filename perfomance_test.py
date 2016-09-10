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

print("############### TEST 2 ################")
# V1: in.
c = 0
i = 0
while i < 1000000:
    if "x" in input:
        c += 1
    i += 1

print("Non-RE")
t3 = time.clock()
print (t3)
# V2: re.search.
i = 0
while i < 1000000:
    if re.search("x", input):
        c += 1
    i += 1

print("RE")
t4 = time.clock()
print (t4)
if(t3 < t4):
    print "Non-RE is faster."
else:
    print ("RE is faster.")
