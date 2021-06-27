#!/usr/bin/env python

import sys
import os
import re


for line in sys.stdin:
  words = filter(None, re.split('\W+', line.lower()))
  for word in words:
    print "%s\t%s\t1" % (word,os.environ['mapreduce_map_input_file'])
    