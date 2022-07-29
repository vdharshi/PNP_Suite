#!/usr/bin/python3
import Global_Var
import csv
import time
print("Executing PPM_017")
print("Test Case ID PPM_017: Check PG STATUS for OTG")
time.sleep(5)
file1=open ("/sys/kernel/debug/pmc_core/substate_live_status_registers",'r')
string1 ='OTG_PG_STS'
index = 0
for line in file1:
 index=index+1
 if string1 in line:
  s=line.replace(" ","")
  n=len(s)
  if '1' in s[n-2]:
    print("SUCCESS")
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     data=["Pch_pm,PPM_017,""SUCCESS, OTG_PG_STS STATUS is OFF"]
     writer=csv.writer(f)
     writer.writerow(data)
     break
  elif '0' in s[n-2]:
    print("FAILURE")
    with open(Global_Var.result_path/'A.csv', 'a') as f:
     data=["Pch_pm,PPM_017,""FAILURE,OTG_PG_STS STATUS IS ON"]
     writer=csv.writer(f)
     writer.writerow(data)
     break
file1.close()
time.sleep(5)
   