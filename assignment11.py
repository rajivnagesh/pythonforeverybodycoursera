#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing up the integers.



import re
file=open('regex_sum_273526.txt', 'r')
sum=0

for line in file:
    x=re.findall('[0-9]+',line)
    for y in x:
        sum=sum+int(y)

print(sum)

# OUTPUT is 329494
