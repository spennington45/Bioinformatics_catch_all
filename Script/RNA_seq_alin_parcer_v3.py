


from glob import glob
import string

file_glob = glob("/scratch/smpenni/full_21/Sequences")

get_next = False
for file_name in file_glob:
    for line in open(file_name,'r'):
        if int:
	     get_next = True
        elif len < 50 in line:
             print(line)
        else:
             get_next = True
        

