#!/usr/bin/python3
import os
import csv
import Global_Var

print("Executing Test Case thermal_001")
print("Test Case ID thermal_001: Information: Reads PL1 from sysfs")
with open("/sys/class/powercap/intel-rapl/intel-rapl:0/constraint_0_power_limit_uw", 'r') as f:
 p=f.read()
 print(p[:-1])
 PL1=((int(float(p)))/1000000)
 print(f"PL1={PL1}")
 print("INFORMATION")
 with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_001","INFORMATION",f"PL1(SYS_FS)={PL1}"]
  writer=csv.writer(a)
  writer.writerow(data)
