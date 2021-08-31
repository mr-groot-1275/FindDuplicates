import os
from hashlib import md5
import sys

if len(sys.argv) == 1:
    print("Example: python find.py /paht/to/work/dir")
    sys.exit(0)

work_dir = sys.argv[1]
duplicates_list = {}


for root, dirs, files in os.walk(work_dir):
    for f in files:
        f_name = os.path.join(root, f)
        f_hash = md5(open(f_name, 'rb').read()).hexdigest()

        if f_hash not in duplicates_list:
            duplicates_list[f_hash] = [f_name]
        else:
            duplicates_list[f_hash].append(f_name)


for k in duplicates_list:
    if len(duplicates_list[k]) > 1:
        print(k)
        for v in duplicates_list[k]:
            print(f"  -->{v}")
