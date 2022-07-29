#!/usr/bin/python3
import re
import os
import csv
import time
import Global_Var
print("Test Case ID PS_018: tracing for profiling the CPU/GPU load")
ctr=0
b=os.popen("/home/scripts/rdmsr -f 0:0 0X770").read()
if b[0]=='1':
  print("PS_018,SUCCESS,HW P-state is supported")
  ctr=ctr+1
  os.popen("echo > /sys/kernel/debug/tracing/set_event")
  os.popen("echo > /sys/kernel/debug/tracing/trace")
  os.popen("echo 32768 > /sys/kernel/debug/tracing/buffer_size_kb")
  os.popen("echo 1 > /sys/kernel/debug/tracing/events/enable")
  os.popen("echo 1 > /sys/kernel/debug/tracing/tracing_on")
  os.popen("echo 0 > /sys/kernel/debug/tracing/tracing_on")
  with open(Global_Var.result_path/"ftrace-data.csv",'w')as f:
    s=os.popen("cat /sys/kernel/debug/tracing/trace").read()
    f.write(s)
  d=os.path.getsize(Global_Var.result_path/"ftrace-data.csv")
  if d!=0:
    print("PS_018,SUCCESS,ftrace data is supported")
    ctr=ctr+1
  else:
    print("PS_018,FAILURE,ftrace data is not supported")
else:
  print("PS_018,FAILURE,HW P-state is not supported")
  
if ctr==2:
 print("SUCCESS")
 data = ["p_states","PS_018","SUCCESS","HWP enabled and ftrace is supported"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
elif ctr==1:
 pritn("HWP enabled but ftrace is not supported")
 data = ["p_states","PS_018","FAILURE","HWP enabled but ftrace is not supported"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["P_states","PS_018","FAILURE","HWP is not enabled itself for ftrace"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)  
