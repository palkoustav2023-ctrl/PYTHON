#Program to use OS Module.
import os
path = "C:\\"
for item in os.listdir(path):
    print(item)