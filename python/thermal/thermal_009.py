#!/usr/bin/python3
import os
import csv
import Global_Var
RDMSR_STATUS=0
print("Executing Test Case thermal_009")
print("Test Case ID thermal_009: Information: Reads PL1 Time Window from MSR")
x = os.popen("/home/scripts/rdmsr -d --bitfield 23:22 0x610").read()
y = os.popen("/home/scripts/rdmsr -d --bitfield 21:17 0x610").read()
x=int(float(x))
y=int(float(y))
PLW=(((1+(x/4))*(2**y))/(2**10))
print("PL1 Time Window=",PLW)
print("INFORMATION")
with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_009","INFORMATION",f"PL1 Time Window(MSR) = {PLW}"]
  writer=csv.writer(a)
  writer.writerow(data)
