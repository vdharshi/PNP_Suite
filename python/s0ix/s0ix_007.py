#!/usr/bin/python3
import os
import Global_Var
import csv
import time
print("Test Case ID s0ix_007: Confirm that the platform goes into s0ix after display is turned on and off")
print("Please wait display will go off and wake after RTC alarm of 1 minute")
with open ("/var/lib/power_manager/suspend_to_idle", 'w') as a:
 a.write("1")
x=os.popen("restart powerd").read()
print(x[:-1])
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
with open ("/sys/kernel/debug/pmc_core/slp_s0_residency_usec", 'r') as a:
 count=a.readline()
 print("count=",count[:-1])
print("Please wait display will go off and wake after RTC alarm of 1 minute")
with open ("/sys/class/rtc/rtc0/wakealarm", 'w') as a:
 x=os.popen("date '+%s' -d '+ 60 seconds'").read()
 a.write(x)
os.popen("set_power_policy --ac_screen_off_delay=30 --battery_screen_off_delay=30")
time.sleep(80)
print("Please wait display will go off and wake after 1 minute")
x=os.popen("restart powerd").read()
print(x[:-1])
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
with open ("/sys/kernel/debug/pmc_core/slp_s0_residency_usec", 'r') as a:
 count1=a.readline()
 print("count1=",count1[:-1])
if count1 > count:
   print(f"S0ix_007:  count before S0ix iteration = {count[:-1]} , count after S0ix iteration = {count1[:-1]}")
   print('SUCCESS')
   data = ["s0ix_states","s0ix_007","SUCCESS on powerd_dbus_suspend"]
   with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
    print(f"S0ix_007:  count before S0ix iteration = {count[:-1]}, count after S0ix iteration = {count1[:-1]}")
    print('FAILURE')
    data = ['s0ix_states','s0ix_007''FAILURE','S0ix count is not incrementing as expected']
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
