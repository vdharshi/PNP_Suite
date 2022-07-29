#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_030")
print("Test Case ID display_30: Checks display counter")

with open("/sys/module/i915/parameters/enable_dc",'r') as f:
 var=f.read()

print(var[:-1])
if var[0]==1:
    data = ["display","display_030","SUCCESS",f"display counter is {var}"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    data = ["display","display_030","FAILURE","dispaly counter is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
