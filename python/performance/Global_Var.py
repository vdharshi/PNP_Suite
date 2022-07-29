from pathlib import Path
import os
global result_path
global func_config_path
global max_no_of_cores
result_path = Path("""/home/python/Results""")
func_config_path=Path("""/home/python/config""")
x=os.popen("cat /proc/cpuinfo").read()
with open(result_path/'B.txt','w') as f:
 f.write(x)
with open(result_path/'B.txt','r') as f:
 index=0
 ctr=0
 for line in f:
  index=index+1
  if 'processor' in line:
   ctr=ctr+1
  else:
   continue
 max_no_of_cores=ctr
