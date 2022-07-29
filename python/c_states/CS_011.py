#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID CS_011: Checks whether C-state counters usage increases before and after S0ix transition")


print("BEFORE S0IX: list the usage values of each state")
with open(Global_Var.result_path/"usage_1.txt","w")as f:
  d=os.popen("cat /sys/devices/system/cpu/cpu*/cpuidle/state*/usage").read()
  f.write(d)
ctr=0
counter=os.popen(f"cat {Global_Var.result_path}/usage_1.txt | wc -l | tr -d ' '").read()
states=os.popen("ls /sys/devices/system/cpu/cpu0/cpuidle/ | wc -w").read()
with open("/var/lib/power_manager/suspend_to_idle",'w')as f:
  f.write('1')
os.system("restart powerd")
time.sleep(10)
os.system("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)

print("AFTER S0IX: list the usage values of each state")
with open(Global_Var.result_path/"usage_1.txt","w")as f:
  d=os.popen("cat /sys/devices/system/cpu/cpu*/cpuidle/state*/usage").read()
  f.write(d)
i=0
counter=int(counter)
while (i<counter):
  usage1=os.popen(f"cat {Global_Var.result_path}/usage_1.txt | awk 'NR=='{i}+1 'print $1'").read()
  print(f"usage1={usage1}")
  usage2=os.popen(f"cat {Global_Var.result_path}/usage_2.txt | awk 'NR=='{i}+1 ").read()  
  print(f"usage2={usage2}")
  cpu=(i/states)
  print(cpu)
  state=(i%states)
  print(state)
  if usage2[:-1]>=usage1[:-1]:
    ctr=ctr+1
    print(f"SUCCESS: cpu{cpu} state{state} counter got incremented")
  else:
    print("FAILURE: cpu{cpu} state{state} counter didn't get incremented")
  i=i+1
time.sleep(1)
if ctr==counters:
 print("SUCCESS")
 data = ["c_states","CS_011","SUCCESS","C-state counters usage increases before and after S0ix transition"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_011","FAILURE","C-state counters usage doesnot increase before and after S0ix transition"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    
