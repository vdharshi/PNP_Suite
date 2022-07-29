#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Executing DPM_011")
count=4
total=os.popen("lspci | wc -l").read()
total=int(total[:-1])
if total > count:
 c= os.popen("lspci | sed -n '4'p | cut -d ':' -f3 | tr -d ' '").read()
 print(f"check runtime status of {c[:-1]} pci device")
 d=os.popen("lspci | sed -n '4'p | cut -d ' ' -f1  | sed 's/0/0000:0/'").read()
 with open(f"/sys/bus/pci/devices/{d[:-1]}/power/runtime_status")as f:
  s=f.read()
  print(s) 
 if s[:-1] == 'suspended':
  print("SUCCESS")
  data = ["Device_pm","DPM_011","SUCCESS",f"{c[:-1]} pci device is in runtime suspended state when in idle"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 else:
  print("FAILURE")
  data=["Device_pm","DPM_011",f"{c[:-1]} pci device is not in runtime suspended state when in idle"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  data=["Device_pm","DPM_011","FAILURE,PCI device NA"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
