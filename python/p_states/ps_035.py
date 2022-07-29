import os
import csv
import Global_Var
import time
print("Test Case ID PS_035: The platform should support HW P-states (if available)")
data=os.popen("dmesg | grep 'intel_pstate: HWP enabled'").read()
with open(Global_Var.result_path/"HWP.txt",'w+') as f:
 f.write(data)
s=os.path.getsize(Global_Var.result_path/"HWP.txt")
if s != 0:
 print("SUCCESS")
 data = ["p_states","PS_035","SUCCESS","HW P-state is supported"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE")
 data = ["p_states","PS_035","FAILURE","HW P-state is not supported"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 
