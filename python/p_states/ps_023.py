import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_023:Turbo feature is enabled or not. if supported, should be enabled")
print("check no_turbo is 0 or not, if enabled, it should be 0")
with open("/sys/devices/system/cpu/intel_pstate/no_turbo",'r') as f:
 val=f.read()
if val[:-1]=='0':
 print("SUCCESS: Turbo feature is enabled")
 data = ["p_states","PS_023","SUCCESS","Turbo feature is enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE: Turbo feature is not enabled")
 data = ["p_states","PS_023","FAILURE","Turbo feature is not enabled"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 
