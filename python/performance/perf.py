import os
value=os.popen("/home/scripts/rdmsr -d --bitfield 14:0 0x610").read()
print(value)
