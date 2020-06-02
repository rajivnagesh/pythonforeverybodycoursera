#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import re


url = 'http://py4e-data.dr-chuck.net/comments_273528.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)

#Output is 2340
