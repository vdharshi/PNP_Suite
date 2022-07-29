#!/usr/bin/python3
import time
import csv
import Global_Var
print("Test Case ID graphics_009: Displays total numbers of EUs")
time.sleep(5)
print("check total number of EUs")
with open("/sys/kernel/debug/dri/0/i915_sseu_status", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "EU Total" in line:
    e=line[-3:-1]
    break
print(e)
if e != '0':
  print('SUCCESS')
  data = ["graphics","graphics_009","SUCCESS",f" Total number of EUs are {e}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
else:
  print('FAILURE')
  data = ["graphics","graphics_008","FAILURE"," ERROR"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
    
