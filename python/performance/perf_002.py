#1/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID perf_002: coreboot s3 resume time should be < 350ms")
time.sleep(5)
print("putting DUT into S3 and will wake up by 1 minute")
with open("/var/lib/power_manager/suspend_to_idle", 'w')as f:
 f.write('0')
os.popen("restart powerd").read()
time.sleep(10)
os.popen("powerd_dbus_suspend --wakeup_timeout=60").read()
time.slepp(5)
s3_resume_time=os.popen("cbmem -T | tail -1 | awk '{print $2}'")
s3_resume_time=(int(s3_resume_time))/1000
print(f"s3_resume_time:{s3_resume_time}")
if s3_resume_time<= 350:
  print("SUCCESS")
  data = ["performance","perf_002","SUCCESS",f"coreboot s3 resume time is {s3_resume_time} that is <= 350ms"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
  print("FAILURE")
  data=["performance","perf_002","FAILURE",f"coreboot s3 resume time is {s3_resume_time} that is not <= 350ms"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)