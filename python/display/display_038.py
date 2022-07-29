#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_038")
print("Test Case ID display_038: Checks and displays total display connectors")
t=[]
with open("/sys/kernel/debug/dri/0/i915_display_info",'r') as f:
 index=0
 ctr=0
 for line in f:
  index=index+1
  if "CONNECTOR:" in line:
   ctr=ctr+1
   t.append(line[1:20])
print(ctr)
if ctr!=0:
    print("SUCCESS")
    data = ["display","display_038","SUCCESS",f"Toatl {ctr} display connectors namely {t}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_038","FAILURE","Sysfs entry  NA"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
