# Author:Colin

import sys
import os

print(sys.path) 
print(sys.argv) 

cmd_res = os.system("ls")
print("--->",cmd_res)
cmd_res = os.popen("ls").read()
print("--->",cmd_res)

os.mkdir("new_dir")

msg = "I live to amuse."
print(msg)