#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    # Remove whitespace either side
    line = line.strip()
    word, count = line.split('\t')

    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# output the last word
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))
