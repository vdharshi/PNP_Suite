#!/usr/bin/python3
import os
import csv
import Global_Var
RDMSR_STATUS=0
print("Executing Test Case thermal_010")
print("Test Case ID thermal_010: Information: Reads PL2 Time Window from MSR")
x = os.popen("/home/scripts/rdmsr -d --bitfield 55:54 0x610").read()
y = os.popen("/home/scripts/rdmsr -d --bitfield 53:49 0x610").read()
x=int(float(x))
y=int(float(y))
PLW=(((1+(x/4))*(2**y))/(2**10))
print("PL1 Time Window=",PLW)
print("INFORMATION")
with open(Global_Var.result_path/'A.csv', 'a') as a:
  data=["thermal","thermal_010","INFORMATION",f"PL2 Time Window(MSR) = {PLW}"]
  writer=csv.writer(a)
  writer.writerow(data)
