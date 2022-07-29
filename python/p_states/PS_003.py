#!/usr/bin/python3
import os
import csv
import Global_Var
import time
max_cpu=Global_Var.max_no_of_cores
print("Test Case ID PS_003: Check whether the platform allows to lock all supported frequencies")
flag=0
ctr=0
i=0
freq=os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies | tr -d '\r' | wc -w | tr -d ' '").read()
print(freq)

