#In this assignment you will write a Python program that expands on https://www.py4e.com/code3/urllinks.py.
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
#scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times,
#and report the last name you find.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

#url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url=input('Enter URL:')
count=int(input('Enter count:'))
position=int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup=BeautifulSoup(html,'html.parser')
href=soup('a')

#print(href)

for i in range(count):
    link=href[position].get('href',None)
    print(href[position].contents[0])
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html,'html.parser')
    href=soup('a')
