#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Executing DPM_040")
print("check whether every intel lpss driver's runtime status is suspended or not")
open(Global_Var.result_path/'kerneldriver.txt','w').close()
open(Global_Var.result_path/'lpss.txt','w').close()
open(Global_Var.result_path/'run_suspend.txt','w').close()
open(Global_Var.result_path/'run_not_suspend.txt','w').close()
a=0
b=0
with open(Global_Var.result_path/'kerneldriver.txt','w')as f:
 d=os.popen("lspci -vvv | grep -i 'Kernel driver in use:' | cut -f 2 -d ':' | tr -d ' ' | sort -u").read()
 f.write(d)
time.sleep(2)
with open(Global_Var.result_path/'kerneldriver.txt','r')as f:
 index=0
 for line in f:
  index=index+1
  if 'intel-lpss'in line:
   print(f"kernel driver is {line[:-1]}")
   with open(Global_Var.result_path/'lpss.txt','a')as f:
    d=os.popen(f"ls -l /sys/bus/pci/drivers/{line[:-1]}/ | grep -i 'devices' | cut -f 5,6,7 -d '/' | tr -d ' '").read()
    f.write(d)
   with open(Global_Var.result_path/'lpss.txt','r')as f:
    index=0
    for line in f:
     index=index+1
     status=os.popen(f"cat /sys/{line[:-1]}/power/runtime_status").read()
     print(f"runtime_status for {line[:-1]} is {status}")
     time.sleep(2)
     if status[:-1]=='suspended':
       with open(Global_Var.result_path/'run_suspend.txt','a')as f:
        f.write(line)
       a=a+1
     else:
       with open(Global_Var.result_path/'run_not_suspend.txt','a')as f:
        f.write(line)
       b=b+1
  else:
   print(f"Kernel driver is {line[:-1]} (not intel-lpss)")
s=os.path.getsize(Global_Var.result_path/'run_not_suspend.txt')
c=a+b
if s==0:
  print("SUCCESS")
  data = ["Device_pm","DPM_040","SUCCESS",f"All {a} intel-lpss Driver is in runtime suspended state when in idle"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data=["Device_pm","DPM_040","FAILURE",f"out of {c} intel-lpss drivers {b} not in runtime suspended state when in idle"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
