#!/usr/bin/python

import sys

# Input takes from standard input for myline in sys.stdin:

for line in sys.stdin:

   line = line.strip()
   words = line.split()

   for word in words:
      if word == 'F':
         words[2] = 0
         words[3] = 0


   print(words[1]+"{visit}"+"\t"+str(words[2]))
   print(words[1]+"{size}"+"\t"+str(words[3]))