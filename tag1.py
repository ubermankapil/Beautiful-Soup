import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Jackie.html').read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
x =list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   x.append(y)
print x 

fhand = urllib.urlopen(x[17])
soup = BeautifulSoup(fhand)
tags = soup('a')
j =list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   j.append(y)
print j 

fhand = urllib.urlopen(j[17])
soup = BeautifulSoup(fhand)
tags = soup('a')
k =list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   k.append(y)
print k

fhand = urllib.urlopen(k[17])
soup = BeautifulSoup(fhand)
tags = soup('a')
l=list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   l.append(y)
print l

fhand = urllib.urlopen(l[17])
soup = BeautifulSoup(fhand)
tags = soup('a')
m=list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   m.append(y)
print m

fhand = urllib.urlopen(m[17])
soup = BeautifulSoup(fhand)
tags = soup('a')
n=list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   n.append(y)
print n

print ("ABD")

fhand = urllib.urlopen(n[17])
soup = BeautifulSoup(fhand)
tags = soup('a')
o=list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   o.append(y)
print o





