#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced,
#The program reads through the dictionary using a maximum loop to find the most prolific committer.

fname=input('Enter file:')
#if len(fname) < 1:
    #name='mbox-short.txt'

fhandle=open(fname,'r')

sender=dict()

for line in fhandle:
    #word=line.split()
    if line.startswith('From:'):
        sender[line.split()[1]]=sender.get(line.split()[1],0)+1

max_key=None
max_val=None

for key,value in sender.items():
    if max_val is None or max_val < value:
        max_val=value
        max_key=key

print(max_key,max_val)
