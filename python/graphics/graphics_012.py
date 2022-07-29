#!/usr/bin/python3
import time
import csv
import os
import Global_Var
print("Test Case ID graphics_012: Checks MESA version")
time.sleep(1)
x=os.popen("emerge -s mesa-iris").read()
with open(Global_Var.result_path/'mesa.txt','w') as a:
 a.write(x)
with open(Global_Var.result_path/'mesa.txt', 'r') as a:
 index=0
 for line in a:
  index=index+1
  if "version" in line:
    e=line[-11:-1]
    break
print(e)
if e != '0':
  print('SUCCESS')
  data = [ "graphics","graphics_012","SUCCESS",f"MESA version is {e}"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
else:
  print('FAILURE')
  data = ["graphics","graphics_012","FAILURE","Mesa Version not found"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
