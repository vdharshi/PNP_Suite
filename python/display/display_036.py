#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_036")
print("Test Case ID display_036: Checks whether ips is enabled or not")

with open("/sys/module/i915/parameters/enable_ips",'r') as f:
 var=f.read()

print(var[:-1])
if var[0]=='1':
    print("SUCCESS")
    data = ["display","display_035","SUCCESS","ips is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_035","FAILURE","ips is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
