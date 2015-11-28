import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html').read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
x =list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   x.append(y)
print x 


print "ABD"
fhand = urllib.urlopen(x[2])
soup = BeautifulSoup(fhand)
tags = soup('a')
j =list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   j.append(y)
print j 

print "ABD"

fhand = urllib.urlopen(j[2])
soup = BeautifulSoup(fhand)
tags = soup('a')
k =list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   k.append(y)
print k

print "ABD"

fhand = urllib.urlopen(k[2])
soup = BeautifulSoup(fhand)
tags = soup('a')
l=list()
for tag in tags:
   # Look at the parts of a tag
   y = tag.get('href', None)
   l.append(y)
print l











 
