#!/usr/bin/python3
import time
import csv
import Global_Var
print("Test Case ID graphics_011: Check whether Huc is used and its version")
time.sleep(1)
print("check whether Huc is used and its version")
with open("/sys/kernel/debug/dri/0/i915_gpu_info", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "HuC firmware" in line:
    e=line[-10:-5]
    break
print(e)
if e != '0':
  print('SUCCESS')
  data = ["graphics","graphics_011","SUCCESS",f"Huc is active and its version is {e}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
else:
  print('FAILURE')
  data = ["graphics","graphics_011","FAILURE","Huc is inactive"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
    
