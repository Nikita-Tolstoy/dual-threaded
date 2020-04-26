import subprocess
import shlex

cmd ='ls -al'

arg = shlix.split(cmd)
p = subprocess.Popen(arg, strout=subprocess.PIPE, subprocess.STDOUT)
result = p.communicate()[0]
