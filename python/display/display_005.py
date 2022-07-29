#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Test Case ID display_005: Display  should support DRRS Feature")
time.sleep(5)
flag=0
print("check whether i915_drrs_status is enabled or not")
with open("/sys/kernel/debug/dri/0/i915_drrs_status",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "DRRS Supported" in line:
   if "Yes" in line:
    print('SUCCESS')
    data = ["display","display_005","SUCCESS","Display supports DRRS feature"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
     break
   else:
    print('FAILURE')
    data = ["display","display_005","FAILURE","Display doesn't support DRRS feature"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
     break 
  else:
    flag=flag+1
    continue  
if flag==1:
   print("REBOOT")
   data = ["display","display_005","REBOOT","active CRT is required"] 
   with open(Global_Var.result_path/"A.csv",'a') as f:
    writer=csv.writer(f)
    writer.writerow(data)
