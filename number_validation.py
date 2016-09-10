import re
li=['9999999999','999999-999','99999x9999']
for item in li:
 if re.match(r'[8-9]{1}[0-9]{9}',item) and len(item) == 10:
     print 'Yes'
 else:
     print 'No'
