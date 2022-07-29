import glob
import os

list_of_files = glob.glob('intel@192.168.1.7:/home/intel/Downloads/info*.txt') 
print(list_of_files)
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
