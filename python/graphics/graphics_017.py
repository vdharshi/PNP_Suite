#!/usr/bin/python3
import time
import csv
import Global_Var
print("Test Case ID graphics_017: Checks efficient GPU frequency")

with open("/sys/kernel/debug/dri/0/i915_frequency_info", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "efficient" in line:
    e=line[-8:-5]
   
if e != '0':
  print('SUCCESS')
  data = ["graphics","graphics_017","SUCCESS",f"Efficient GPU frequency is {e} MHz"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
else:
  print('FAILURE')
  data = ["graphics","graphics_017","FAILURE","Sys fs NA"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
