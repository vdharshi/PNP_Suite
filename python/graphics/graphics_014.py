#!/usr/bin/python3
import time
import csv
import os
import Global_Var
print("Test Case ID graphics_014: Checks whether Media Compression is enabled")
x=os.popen("intel_reg --binary read 0x70180").read()
with open(Global_Var.result_path/'rbc.txt', 'w') as a:
 a.write(x)
with open(Global_Var.result_path/'rbc.txt', 'r') as a:
 for line in (a.readlines() [-1:]):
  line.replace(" ","")
  g=line[-10:-9]
print("4th bit is",g)
if g == '1':
  print('SUCCESS')
  data = [ "graphics","graphics_014","SUCCESS","Media Compression is enabled" ]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data)  
else:
  print('FAILURE')
  data = ["graphics","graphics_014","FAILURE","Media Compression is disabled"]
  with open(Global_Var.result_path/'A.csv', 'a') as f:
   writer = csv.writer(f)
   writer.writerow(data) 
