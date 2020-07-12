


from glob import glob

file_glob = glob("/scratch/smpenni/full_21/Sequences")

get_next = False
for file_name in file_glob:
    for line in open(file_name,'r'):
        if "A" or "C" or "G" or "T" and line.count > 40 in line:
             get_next = True
        elif line.strip() != "" and get_next:
            get_next = False
            print(line.strip())


