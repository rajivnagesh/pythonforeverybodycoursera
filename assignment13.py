#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib
#and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.

from urllib.request import urlopen
import urllib
import xml.etree.ElementTree as ET

url='http://py4e-data.dr-chuck.net/comments_273530.xml'

#get the content of the url as a string
data=urllib.request.urlopen(url).read()

#transform the string content into an xml tree
tree=ET.fromstring(data)

#find all count elements
counts=tree.findall('comments/comment/count')

#extract the value of each count element and add it to the total
total=0
for count in counts:
    total+=int(count.text)

print('Total:',total)

#Output is - 2617
