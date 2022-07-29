#!/usr/bin/python3
import os
import csv
import Global_Var
RDMSR_STATUS=0
print("Executing Test Case thermal_003")
print("Test Case ID thermal_003: Information: Reads PL1 from MSR")
p = os.popen("/home/scripts/rdmsr -d --bitfield 14:0 0x610").read()
p=int(float(p))
PL1=p/8
print("PL1=",PL1)
print("INFORMATION")
with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_003","INFORMATION",f"PL1(MSR) = {PL1}"]
  writer=csv.writer(a)
  writer.writerow(data)
