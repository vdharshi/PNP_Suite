#!/usr/bin/python3
import os
import csv
import time
import Global_Var
print("Test Case ID perf_067: During stress ng test, check whether scaling frequency is greater than 800 MHz")
os.popen("timeout 60 stress-ng -c 1 --cpu-method idct --metrics-brief")
time.sleep(10)
freq= os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read()
print(freq)
time.sleep(50)
freq=int(freq[:-1])

if freq > 800000:
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

