#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID perf_036: During ido, check Throttling due to VR TDC limit due to RING")
def get_bits_frm_msr(a,b):
  res=os.popen(f"/home/scripts/rdmsr -c --bitfield {a} {b} 2>/dev/null").read()
  rdmsr_status=os.system(f"/home/scripts/rdmsr -c --bitfield {a} {b} 2>/dev/null")
  if rdmsr_status!=0:
    res=0
  print(res)
  return rdmsr_status
cpu_limit=get_bits_frm_msr('6:6',0x6B1)
print(cpu_limit)
if cpu_limit==0:
    print('SUCCESS')
    data = ["performance","perf_036","SUCCESS","During ido No throttling due to VR TDC limit due to RING"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
else:
    print('FAILURE')
    data = ["performance","perf_036","FAILURE","During ido Throttling due to VR TDC limit due to RING"]
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
