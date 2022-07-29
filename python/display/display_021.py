#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_021")
print("Test Case ID display_021: check whether PSR panel are PSR2")
time.sleep(1)
print("check whether psr2?")
with open("/sys/kernel/debug/dri/0/i915_edp_psr_status",'r') as f:
 index=0
 for line in f:
  index=index+1
  stat='/n'
  if "PSR MODE" in line:
   stat=line[-3:-1]
   print("stat:",stat)
   break
if stat=='yes':
    print('SUCCESS')
    data = ["display","display_021","SUCCESS","Display supports PSR2 Panels"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["display","display_021","FAILURE","Display is not supporting PSR2 Panels"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
