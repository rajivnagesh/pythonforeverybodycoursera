fname=input('Enter file name:')
fhand=open(fname)
lst=list()
for line in fhand:
    word=line.rstrip().split()
    for element in word:
        if element in lst:
            continue
        else:
            lst.append(element)

lst.sort()
print(lst)
