#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID perf_048: During stress ng test, check PL2 Throttling due to CPU")
def get_bits_frm_msr(a,b):
  res=os.popen(f"/home/scripts/rdmsr -c --bitfield {a} {b} 2>/dev/null").read()
  rdmsr_status=os.system(f"/home/scripts/rdmsr -c --bitfield {a} {b} 2>/dev/null")
  if rdmsr_status!=0:
    res=0
  print(res)
  return rdmsr_status
os.system("timeout 60 stress-ng -c 1 --cpu-method idct --metrics-brief & sleep 10")
  
cpu_limit=get_bits_frm_msr('11:11',0x64f)
print(cpu_limit)
if cpu_limit==0:
    print('SUCCESS')
    data = ["performance","perf_048","SUCCESS","During stress ng test No PL2 Throttling due to CPU"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["performance","perf_048","FAILURE","During stress ng test PL2 Throttling due to CPU"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
