#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_034")
print("Test Case ID display_034: Checks whether GUC is enabled or not")

with open("/sys/module/i915/parameters/enable_guc",'r') as f:
 var=f.read()
var=int(var[:-1])
print(var)
if var >0:
    print("SUCCESS")
    data = ["display","display_034","SUCCESS","GUC is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_034","FAILURE","GUC is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
