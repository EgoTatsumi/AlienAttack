import os
filename = 'record.txt'
with open(filename, "w") as f:
        f.write('0')
os.system('python alienattack.py')