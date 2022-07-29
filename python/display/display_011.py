#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_011")
print("Test Case ID display_011: Display should support PSR Panels")
time.sleep(5)
print("check whether i915_edp_psr_status is enabled or not")
with open("/sys/kernel/debug/dri/0/i915_edp_psr_status",'r') as f:
 index=0
 for line in f:
  index=index+1
  if "Sink" in line:
    sink=line[-3:-1]
    print("sink:",sink)
    break
  elif "PSR MODE" in line:
   stat=line[-3:-1]
   print("stat:",stat)
   break
 
if sink=='yes' and stat=='yes':
    print('SUCCESS')
    data = ["display","display_011","SUCCESS","Display supports PSR Panels"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_011","FAILURE","Display is not supporting PSR Panels"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
