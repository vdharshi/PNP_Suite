#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_026")
print("Test Case ID display_026: checks whether display port is eDP-1")
with open("/sys/kernel/debug/dri/0/i915_display_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "status: connected" in line:
   dp=line[15:20]
   print(dp)
   break
if dp == 'eDP-1':
    print('SUCCESS')
    data = ["display","display_026","SUCCESS",f"display port is {dp}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_026","FAILURE",f"display port is {dp}, not eDP-1"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
