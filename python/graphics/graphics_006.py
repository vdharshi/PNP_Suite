#!/usr/bin/python
import Global_Var
import time
import csv
print("Test Case ID graphics_006: GFX should support frame buffer compression feature")
time.sleep(5)
print("check whether i915_fbc_status is enabled or not")
with open("/sys/module/i915/parameters/enable_fbc",'r')as f:
 fbc=f.read()
if fbc[0]==1:
  print('SUCCESS')
  data = ["graphics","graphics_006","SUCCESS","GFX supports frame buffer compression feature"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data)
 
else:
  print('FAILURE')
  data = ["graphics","graphics_006","FAILURE","GFX is not supporting frame buffer compression feature"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data)
time.sleep(5)
