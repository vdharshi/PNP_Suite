#!/usr/bin/python3
import time
import csv
import Global_Var
print("Test Case ID graphics_010: Check whether GPU is idle")
time.sleep(1)
print("check whether GPU is idle")
with open("/sys/kernel/debug/dri/0/i915_runtime_pm_status", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "GPU" in line:
    e=line[-4:-1]
    break
if e =='yes':
  print('SUCCESS')
  data = ["graphics","graphics_010","SUCCESS","GPU is idle"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
else:
  print('FAILURE')
  data = ["graphics","graphics_010","FAILURE","GFX is not in idle"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
    
