name = input("Enter file:")
handle = open(name)
dd=dict()
for line in handle:
    if line.startswith("From "):
     yy=line.split()
     gg=yy[1]
     dd[gg]=dd.get(gg,0)+1

val=None
num=None
for aaa,bbb in dd.items():
    if val is None or bbb>val:
        num=aaa
        val=bbb
print(num,val)

#Write a program to read through
the mbox-short.txt and figure out who
has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the
second word of those lines as the person who sent 
the mail. The program creates a Python dictionary that
maps the sender's mail address to a count of the
number of times they appear in the file.
After the dictionary is produced, the
program reads through the dictionary using a maximum
loop to find the most prolific committer.
