#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_026: Turbostat & powertop should be support for the platform")
os.system(f"powertop -t 30 -C{Global_Var.result_path}/powertop_CS_026.csv")
os.popen(f"timeout 10 turbostat -o  {Global_Var.result_path}/turbostat_CS_026.csv")
d=os.path.getsize(f"{Global_Var.result_path}/powertop_CS_026.csv")
c=os.path.getsize(f"{Global_Var.result_path}/turbostat_CS_026.csv")
if c!=0 and d!=0:
  print("CS_026: SUCCESS")
  data = ["c_states","CS_026","SUCCESS","Turbostat & powertop are supported for the platform"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("CS_026: FAILURE")
  data = ["c_states","CS_026","FAILURE","Turbostat & powertop are not supported for the platform"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data) 
