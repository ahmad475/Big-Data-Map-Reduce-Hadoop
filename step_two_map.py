#!/usr/bin/env python

import sys
import os
import re

for line in sys.stdin:
  print "%s\t1" % line.strip()

