#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID perf_053: During stress ng test, check RATL throttling due to GPU")
def get_bits_frm_msr(a,b):
  res=os.popen(f"/home/scripts/rdmsr -c --bitfield {a} {b} 2>/dev/null").read()
  rdmsr_status=os.system(f"/home/scripts/rdmsr -c --bitfield {a} {b} 2>/dev/null")
  if rdmsr_status!=0:
    res=0
  print(res)
  return rdmsr_status
os.system("timeout 60 stress-ng -c 1 --cpu-method idct --metrics-brief & sleep 10")
  
cpu_limit=get_bits_frm_msr('5:5',0x6B0)
print(cpu_limit)
if cpu_limit==0:
    print('SUCCESS')
    data = ["performance","perf_053","SUCCESS","During stress ng test No RATL throttling due to GPU"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["performance","perf_053","FAILURE","During stress ng test RATL throttling due to GPU"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
