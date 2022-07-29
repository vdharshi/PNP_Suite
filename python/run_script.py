import re
import os
import csv
import time
p=input("enter path:")
with open("/home/run.txt",'w+')as f:
 d=os.popen(f"ls {p}").read()
 f.write(d)
with open("/home/run.txt",'r')as f:
 index=0
 for line in f:
  index=index+1
  os.popen(f"python3 {line[:-1]}").read()
print("done")
