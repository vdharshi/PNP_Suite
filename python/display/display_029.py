#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_029")
print("Test Case ID display_29: Checks whether runtime power is enabled or not")
with open("/sys/kernel/debug/dri/0/i915_runtime_pm_status",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "Runtime" in line:
   var1=line[-8:-1]
   break


print(var1)
if var1== 'enabled':
    print('SUCCESS')
    data = ["display","display_029","SUCCESS","Runtime power is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_029","FAILURE","Runtime power is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
