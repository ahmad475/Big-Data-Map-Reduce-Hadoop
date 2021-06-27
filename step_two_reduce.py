#!/usr/bin/env python

import sys
import math

def logifier(list_elem,total_d):
  word,book,num_word=list_elem.strip().split()
  tf =float(num_word)
  tf_idf = float(tf) * float(math.log(20/total_d))
  return float(tf_idf)

present_w = None
total_d = None
keyval_list = []

for line in sys.stdin:
  word,book,num_word,total_doc = line.strip().split()
  first_part = "%s\t%s\t%s" %(word,book,num_word)
  if word == None:
    present_w = word
    total_d = eval(total_doc)
    keyval_list.append(first_part)
  elif present_w == word:
    total_d += eval(total_doc)
    keyval_list.append(first_part)
  else:
    for list_elem in keyval_list:
      word1,book1,num_word1=list_elem.strip().split()
      print "%s,%s\t%10.6f" % (word1,book1,logifier(list_elem,total_d))
    present_w = word
    total_d = eval(total_doc)
    keyval_list = [first_part]
for list_elem in keyval_list:
  word1,book1,num_word1=list_elem.strip().split()
  print "%s,%s\t%10.6f" % (word1,book1,logifier(list_elem,total_d))

