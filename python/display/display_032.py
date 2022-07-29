#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_032")
print("Test Case ID display_032: Checks whether display mst is enabled or not")

with open("/sys/module/i915/parameters/enable_dp_mst",'r') as f:
 var=f.read()

print(var[:-1])
if var[0]=='Y':
    print("SUCCESS")
    data = ["display","display_031","SUCCESS","display mst is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_031","FAILURE","dispaly mst is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
