#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID perf_068: During stress ng test, check whether cpu frequency is throttling")
os.system("timeout 60 stress-ng -c 1 --cpu-method idct --metrics-brief")

with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq",'r')as f:
  cf=f.read()
  print("cur freq="+cf)
with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq",'r')as f:
  mf=f.read()
  print("max freq="+mf)

time.sleep(80)
mf=int(mf[:-1])
cf=int(cf[:-1])

if mf > cf:
  f=mf-cf
  print(f) 
else:
 f=0
if f>100:
  print('SUCCESS')
  data = ["performance","perf_067","SUCCESS","During stress ng test scaling frequency is greater than 800 MHz"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["performance","perf_067","FAILURE","During stress ng test scaling frequency is not greater than 800 MHz"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)

 
