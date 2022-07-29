#!/usr/bin/python3
import os
import Global_Var
import csv
import time
print("Executing Test Case S0ix_024")
print("Test Case ID S0ix_024: The platform should support s0ix and should comeout of S0ix after RTC wake alarm")
with open ("/sys/kernel/debug/pmc_core/slp_s0_residency_usec", 'r') as a:
 count=a.readline()
 print("count=",count[:-1])
 count=int(float(count[:-1]))
print("checking counter value BEFORE S0IX")
with open ("/sys/kernel/debug/suspend_stats", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "success" in line:
   n=len(line)
   val=line[-3:-1]
   break
  
val=int(float(val))
print("Please wait display will go off and wake after 1 minute")
with open ("/sys/class/rtc/rtc0/wakealarm", 'w') as a:
 x=os.popen("date '+%s' -d '+ 60 seconds'").read()
 a.write(x)  
with open ("/var/lib/power_manager/suspend_to_idle", 'w') as a:
 a.write("1")
x=os.popen("restart powerd").read()
print(x[:-1])
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
with open ("/sys/kernel/debug/pmc_core/slp_s0_residency_usec", 'r') as a:
 count1=a.readline()
 print("count1=",count1[:-1])
 count1=int(float(count1[:-1]))
with open ("/sys/kernel/debug/suspend_stats", 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "success" in line:
   n=len(line)
   val1=line[-3:-1]
   break 
val1=int(float(val1))


if count1 > count and val1 >val:
   print(f"S0ix_024,SUCCESS,count before S0ix iteration = {count}:{val} , count after S0ix iteration = {count1}:{val1}")
   print('SUCCESS')
   data = ['s0ix_states','S0ix_024','SUCCESS','S0ix count is incrementing as expected']
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
    print('FAILURE')
    data = ['s0ix_states','S0ix_024','FAILURE','S0ix count is not incrementing as expected']
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
