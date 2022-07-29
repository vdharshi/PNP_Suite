#!/usr/bin/python3
import os
import sys
import csv
import Global_Var
print("executing DPM_002")

print("all devices, when are never used on platform, should always be in D3 state & power gate.")
dev_dri_nme=['SATA', 'CSE', 'ISH', 'exi', 'smb', 'gbe']
pg=0
i=0
while(i<6):
	f=os.popen(f"cat /sys/kernel/debug/pmc_core/pch_ip_power_gating_status | grep -i '{dev_dri_nme[i]}'").read()

	if  'Off' in f:
	 pg=pg+1
	 print(f"SUCCESS: {dev_dri_nme[i]} is getting power gated")
	else:
	 print(f"FAILURE: {dev_dri_nme[i]} is not getting power gated")
	i=i+1 
print(pg)
if pg ==6:
 print("SUCCESS")
 data = ["Device_pm","DPM_002","SUCCESS","All the device drivers (Device list - SATA; CSE; ISH; GBE; SMB; EXI) are getting power gated"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE") 
 data = ["Device_pm","DPM_002","FAILURE","All the device drivers (Device list - SATA; CSE; ISH; GBE; SMB; EXI) are not getting power gated"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
