#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_035")
print("Test Case ID display_035: Checks whether hangcheck is enabled or not")

with open("/sys/module/i915/parameters/enable_hangcheck",'r') as f:
 var=f.read()

print(var[:-1])
if var[0]=='Y':
    print("SUCCESS")
    data = ["display","display_035","SUCCESS","hangcheck is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_035","FAILURE","hangcheck is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
