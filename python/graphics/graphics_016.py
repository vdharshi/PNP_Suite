#!/usr/bin/python3
import time
import csv
import Global_Var
print("Test Case ID graphics_016: Checks maximum GPU frequency")

with open("/sys/kernel/debug/dri/0/i915_frequency_info", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "Max freq" in line:
    e=line[-8:-5]
    break
if e != '0':
  print('SUCCESS')
  data = ["graphics","graphics_016","SUCCESS",f"maximum GPU frequency is {e} MHz"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
else:
  print('FAILURE')
  data = ["graphics","graphics_016","FAILURE","Sys fs NA"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
