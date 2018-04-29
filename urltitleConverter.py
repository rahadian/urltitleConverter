#save as csv
import re
import string
from slugify import slugify

f = open('db.txt', 'r')
f2=open('db.csv','w')
for line in iter(f):
	z=slugify(line)
	x=str.title(z)
	f2.write(x)
	f2.write("\n")
	print x
f.close()
f2.close()
