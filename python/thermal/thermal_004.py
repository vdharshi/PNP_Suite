#!/usr/bin/python3
import os
import csv
import Global_Var
RDMSR_STATUS=0
print("Executing Test Case thermal_004")
print("Test Case ID thermal_004: Information: Reads PL2 from MSR")
p = os.popen("/home/scripts/rdmsr -d --bitfield 46:32 0x610").read()
p=int(float(p[:-1]))
PL2=p/8
print("PL2=",PL2)
print("INFORMATION")
with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_004","INFORMATION",f"PL2(MSR) = {PL2}"]
  writer=csv.writer(a)
  writer.writerow(data)
