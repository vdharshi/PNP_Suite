import os
import csv
import Global_Var
import time
print("Executing mem_003")
print("Test Case ID mem_003: Displays the memory Speed")
r=os.popen("dmidecode -t memory | grep -i size | awk '{print $2}' | head -1").read()
print(f"Speed is {r[:-1]} MT/S ")
print("INFORMATIVE")
data = ["Memory","mem_003","INFORMATION",f"Memory Speed is {r[:-1]} MT/S"]
with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
