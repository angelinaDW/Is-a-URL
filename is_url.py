'''
Requirements:
1. Starts with http:// or https://
contains at least one .
contains at least one character on either side of the dots

'''
import re

# adding a question mark after a group makes it optional
urlRegex = re.compile('(http(s)?)://(www\.)?((\w)+)\.((\w)+)((/(\S)*)*)?')

# testing
print(urlRegex.search("https://pythex.org")) # match
g= urlRegex.search("https://pythex.org/yesser/yesah") # match
print(g.group())
print(urlRegex.findall("https://pythex.org/yesser/yesah"))