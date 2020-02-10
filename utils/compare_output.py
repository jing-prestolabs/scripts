import os
import sys 
import subprocess

if len(sys.argv) != 3:
    print("Usage: python compare_output.py dir1 dir2")
    exit(1)

dir1=sys.argv[1]
dir2=sys.argv[2]

dir1_files = []
for current_root, dirs, files in os.walk(dir1):
    for f in files:
        dir1_files.append(os.path.join(current_root, f))

dir2_files = []
for current_root, dirs, files in os.walk(dir2):
    for f in files:
        dir2_files.append(os.path.join(current_root, f))

if len(dir1_files) != len(dir2_files):
    print("Different number of files")
else:
    print("Same number of files")

for f1, f2 in zip(dir1_files, dir2_files):
    res = subprocess.run(["diff", f1, f2])
    try:
        res.check_returncode()
    except subprocess.CalledProcessError as err:
        sys.exit(err.cmd)

print("Outputs are identical")
