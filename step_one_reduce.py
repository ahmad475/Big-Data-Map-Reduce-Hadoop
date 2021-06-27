#!/usr/bin/env python

import sys
import os
import re

first_part = None
tot_words = None
for line in sys.stdin:
  word,book,total = line.strip().split('\t')
  front_part = '%s\t%s' % (word,book)
  if first_part == None:
    first_part = front_part
    tot_words = eval(total)
  elif first_part == front_part:
    tot_words += eval(total)
  else:
    print "%s\t%s" % (first_part,tot_words)
    first_part = front_part
    tot_words = eval(total)
print "%s\t%s" % (first_part,tot_words)


