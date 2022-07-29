import os
import csv
import Global_Var
import time
print("Executing mem_001")
print("Test Case ID mem_001: Displays the memory rank")
r=os.popen("dmidecode -t memory | grep -i rank | awk '{print $2}' | head -1").read()
print("rank is ",r)
print("INFORMATIVE")
data = ["Memory","mem_001",f"INFORMATION,Memory Rank is {r[:-1]}"]
with open(Global_Var.result_path/'A.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(data)
