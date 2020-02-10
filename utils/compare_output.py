import os
import sys 
import subprocess

# Perform a file-to-file comparison between all the files in
# the two input directories

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

num_of_files_dir1 = len(dir1_files)
num_of_files_dir2 = len(dir2_files)

if num_of_files_dir1 != num_of_files_dir2:
    print("Different number of files (" + str(num_of_files_dir1) + " vs " + str(num_of_files_dir2) + ")")
else:
    print("Same number of files (" + str(num_of_files_dir1) + ")")

for f1, f2 in zip(dir1_files, dir2_files):
    res = subprocess.run(["diff", f1, f2])
    try:
        res.check_returncode()
    except subprocess.CalledProcessError as err:
        sys.exit(err.cmd)

print("All files are identical")
