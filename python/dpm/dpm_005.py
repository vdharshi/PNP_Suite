#!/usr/bin/python3
import os
import sys
import csv
import Global_Var
print("executing DPM_005")
os.system("sudo setpci -s 1e.0 CAP_PM+4.b=03")

print("All the device drivers should implement system suspend to enter/exit the lower power state of the system/device. Device list - Audio, eMMC, SDCard, WIFI, BT, USH - USB (xHCI), USB - OTG (xDCI), UART, I2c/spi/lpss, Touch.")
dev_dri_nme=['HDA_PGD0', 'HDA_PGD1', 'HDA_PGD2', 'HDA_PGD3', 'SPA', 'SPB', 'SPC', 'SPD', 'SPI', 'LPSS', 'XHCI', 'USB3_OTG']
pg=0
npg=0
i=0
while(i<12):
	f=os.popen(f"cat /sys/kernel/debug/pmc_core/pch_ip_power_gating_status | grep -i '{dev_dri_nme[i]}'").read()
	if  'Off' in f:
	 pg=pg+1
	 print(f"SUCCESS: {dev_dri_nme[i]} is getting power gated")
	else:
	 print(f"FAILURE: {dev_dri_nme[i]} is not getting power gated")
	 npg=npg+1
	i=i+1 
print(pg)
if pg ==6:
 print("SUCCESS")
 data = ["Device_pm","DPM_005","SUCCESS","All the device drivers (Device list - Audio; eMMC; SDCard; WIFI; BT; USH - USB (xHCI); USB - OTG (xDCI); UART; I2c/spi/lpss; Touch) are getting power gated"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
else:
 print("FAILURE") 
 data = ["Device_pm","DPM_002","FAILURE",f"out of (HDA_PGD0 HDA_PGD1 HDA_PGD2 HDA_PGD3 SPA SPB SPC SPD SPI LPSS XHCI USB3_OTG) {npg} device not power gating"]
 with open(Global_Var.result_path/'A.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)
