#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID CS_024: The platform shall support new package state PC2_VOA in display off and freeze")
print("Keep the DUT in IDLE case, make sure you are running the script through Putty")
print("checking new package state PC2_VOA  value")
ctr=0
val=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={val}")
time.sleep(10)
print("Please wait display will go off and wake after RTC alarm of 1 minute")
d=os.popen("echo `date '+%s' -d '+ 60 seconds'`").read()
with open("/sys/class/rtc/rtc0/wakealarm",'w')as f:
 f.write(d)
os.popen("set_power_policy --ac_screen_off_delay=30 --battery_screen_off_delay=30")
time.sleep(80)
print("DUT woken up by RTC alarm")
print("checking new package state PC2_VOA  value after a minute delay")
val1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={val1}")
if val1>val:
 print("SUCCESS on new package state PC2_VOA incrementation for Idle display off")
 ctr=ctr+1
else:
 print("FAILURE on new package state PC2_VOA incrementation for Idle display off")
time.sleep(10)
print("checking new package state PC2_VOA value")
val=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={val}")
with open("/var/lib/power_manager/suspend_to_idle",'w')as f:
 f.write('1')
os.popen("restart powerd").read()
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60")
time.sleep(5)
print("checking new package state PC2_VOA value after a minute delay")
val1=os.popen("cat /sys/kernel/debug/pmc_core/package_cstate_show | grep -i 'Package C2' | cut -f2 -d ':' | tr -d ' ' | tr -d '[[:space:]]'").read()
print(f"value={val1}")
if val1 >val:
 ctr=ctr+1
 print("SUCCESS on new package state PC2_VOA incrementation for freeze")
else:
 print("FAILURE on new package state PC2_VOA incrementation for freeze")
if ctr==2:
 print("SUCCESS")
 data=["c_states","CS_024","SUCCESS","platform supports new package state PC2_VOA in display off and freeze"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["c_states","CS_024","FAILURE","platform donot support new package state PC2_VOA in display off and freeze"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
