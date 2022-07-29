#!/usr/bin/python3
import os
import subprocess
with open("/home/python/pnp_siv.txt",'r')as f:
 index=0
 for line in f:
  index=index+1
  if line[:-1]=='on':
   continue
  elif 'CS_' in line:
   subprocess.call(f'python3 /home/python/c_states/{line[:-1]}.py',shell=True)
  elif 'PS' in line:
   subprocess.call(f'/home/python/p_states/{line[:-1]}.py')
  elif 's0ix' in line:
   subprocess.call(f'/home/python/s0ix/{line[:-1]}.py')
  elif 'display' in line:
   subprocess.call(f'/home/python/display/{line[:-1]}.py')
  elif 'graphics' in line:
   subprocess.call(f'/home/python/graphics/{line[:-1]}.py')
  elif 'dpm' in line:
   subprocess.call(f'/home/python/dpm/{line[:-1]}.py',shell=True)
  elif 'kpm' in line:
   subprocess.call(f'/home/python/kpm/{line[:-1]}.py')
  elif 'thermal' in line:
   os.system(f'/home/python/thermal/{line[:-1]}.py')
  elif 'cpu_hp' in line:
   subprocess.call(f'/home/python/cpu_hp/{line[:-1]}.py')
  elif 'mem' in line:
   subprocess.call(f'/home/python/memory/{line[:-1]}.py')
  else:
   print("test case not listed")

