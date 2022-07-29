#!/usr/bin/python3
import os
import csv
import Global_Var
print("Executing Test Case thermal_002")
print("Test Case ID thermal_002: Information: Reads PL2 from sysfs")
with open("/sys/class/powercap/intel-rapl/intel-rapl:0/constraint_1_power_limit_uw", 'r') as f:
 p=f.read()
 print(p[:-1])
 PL2=((int(float(p)))/1000000)
 print(f"PL2={PL2}")
 print("INFORMATION")
 with open(Global_Var.result_path/'A.csv', 'a') as a:
   data=["thermal","thermal_002","INFORMATION",f"PL2(SYS_FS) = {PL2}"]
   writer=csv.writer(a)
   writer.writerow(data)
