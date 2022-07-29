#!/usr/bin/python3
import os
import csv
import Global_Var
print("Executing display_002")
print("Test Case ID display_002: checks whether display resolution is 1920x1280")
with open("/sys/kernel/debug/dri/0/i915_display_info",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "mode" in line:
   
    res=line[37:45]
    print(res)
    break   
   
if res == '1920x1280':
    print('SUCCESS')
    print(a)
    data = ["display","display_002","SUCCESS",f" display resolution is {res}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_002","FAILURE",f"display resolution is {res} not 1920*1280"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data) 
