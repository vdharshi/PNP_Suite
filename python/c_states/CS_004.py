#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID CS_004: Verify whether the platform supports c-states sysfs entry or not")
cpu_core=Global_Var.max_no_of_cores
ctr=0
i=0
while(i<cpu_core):
  print(i)
  d=os.popen(f"ls /sys/devices/system/cpu/cpu{i}/cpuidle").read()
  with open(Global_Var.result_path/f"cpu{i}.txt",'w')as f:
   f.write(d)
  state=os.popen(f"ls -l /sys/devices/system/cpu/cpu{i}/cpuidle/ | grep -c ^d").read()
  print("state="+state)
  j=0
  state=int(state[:-1])
  while(j<state):
    actual_var=os.popen(f"grep -o 'state'{j} {Global_Var.result_path}/cpu{i}.txt").read()
    print("act="+actual_var)
    count=2
    count=count+j

    expected_var=os.popen(f"grep -r 'CS_004' {Global_Var.func_config_path}/mofd_config.csv | cut -d',' -f{count}").read()
    print("expected_var="+expected_var)
    if actual_var==expected_var:
      ctr=ctr+1
      print(ctr)
      with open(Global_Var.result_path/"CS_004.txt",'a')as f:
        f.write(f"CS_004_core{i},""SUCCESS,"f"Exp_res: {expected_var},"f"Actual_res: {actual_var},""the platform supports C-ctate sysfs entry")
    else:
      with open(Global_Var.result_path/"CS_004.txt",'a')as f:
        f.write(f"CS_004_core{i},""FAILURE,"f"Exp_res: {expected_var},"f"Actual_res: {actual_var},""the platform don't support C-ctate sysfs entry")
    j=j+1
  i=i+1
print(f"counter={ctr}")
cs=cpu_core*state
if ctr==cs:
 print("SUCCESS")
 data = ["c_states","CS_004","SUCCESS","C-state sysfs entry is supported for every core"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_004","FAILURE","C-state sysfs entry is not supported for every core"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

  
  
  
  
