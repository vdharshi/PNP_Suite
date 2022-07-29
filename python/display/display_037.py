#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_037")
print("Test Case ID display_037: Checks for total number of video command streams")

with open("/sys/kernel/debug/dri/0/i915_engine_info",'r') as f:
 index=0
 ctr=0
 for line in f:
  index=index+1
  if "vcs" in line:
   ctr=ctr+1

print(ctr)
if ctr!=0:
    print("SUCCESS")
    data = ["display","display_037","SUCCESS",f"Total number of VCS are {ctr}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_037","FAILURE","VCS NA"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
