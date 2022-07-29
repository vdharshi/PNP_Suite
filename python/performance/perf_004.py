#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID perf_004: Display resume time in S3 and S0ix should be <= 300ms")
time.sleep(5)
pritn("Please wait display will go off and wake after 1 minute")
with open("/var/lib/power_manager/suspend_to_idle", 'w')as f:
 f.write('0')
os.popen("restart powerd").read()
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60").read()
time.slepp(5)
ctr=0
display_time=os.popen("cat /var/log/messages | grep returned | grep 0000:00:02 | tail -3 | awk '{print $(NF-1)}' | awk '{s+=$1}END{print s}'").read()
s3_display_resume_time=(int(display_time[:-1]))/1000
print(f"s3_display_resume_time: {s3_display_resume_time}")
if s3_display_resume_time <= 300:
 print("SUCCESS")
 ctr=ctr+1
 print("Display resume time in S3 is < 300ms")
else:
 print("Display resume time in S3 is not < 300ms")

print("Please wait display will go off and wake after 1 minute")
with open("/var/lib/power_manager/suspend_to_idle",'w')as f:
 f.write(1)
os.popen("restart powerd").read()
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60").read()
time.slepp(5)
os.popen("cat /var/log/messages | grep returned | grep 0000:00:02 | tail -3 | awk '{print $(NF-1)}' | awk '{s+=$1}END{print s}'").read()
s0ix_display_resume_time=os.popen("cat /var/log/messages | grep returned | grep 0000:00:02 | tail -3 | awk '{print $(NF-1)}' | awk '{s+=$1}END{print s}'").read()
s0ix_display_resume_time=(int(s0ix_display_resume_time))/1000
print(f"s0ix_display_resume_time:{s0ix_display_resume_time}")
if s0ix_display_resume_time <= 300:
 print("SUCCESS")
 ctr=ctr+1
 print("Display resume time in S3 is < 300ms")
else:
 print("Display resume time in S3 is not < 300ms")
if ctr==2:
  print("SUCCESS")
  data = ["performance","perf_004","SUCCESS",f"Display resume time in s0ix is {s0ix_display_resume_time} ms and in s3 is {s3_display_resume_time} ms; <= 300 ms"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data=["performance","perf_004",f"Display resume time in s0ix is {s0ix_display_resume_time} ms and in s3 is {s3_display_resume_time ms}; not <= 300ms"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)