#!/usr/bin/python3
import os
import csv
import Global_Var
import time
print("Executing display_033")
print("Test Case ID display_033: Checks whether display backlight is enabled or not")

with open("/sys/module/i915/parameters/enable_dpcd_backlight",'r') as f:
 var=f.read()
var=int(var[:-1])
print(var)
if var>0:
    print("SUCCESS")   
    data = ["display","display_033","SUCCESS","display backlight is enabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print("FAILURE")
    data = ["display","display_033","FAILURE","dispaly backlight is disabled"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
