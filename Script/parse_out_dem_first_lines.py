


from glob import glob 

file_glob = glob("/scratch/smpenni/SRR934064_seq1ae.fasta.*of150.fasta.blastn")

get_next = False
for file_name in file_glob: 
    for line in open(file_name,'r'):
        if "Sequences producing significant alignments:" in line: 
             get_next = True 
        elif line.strip() != "" and get_next: 
            get_next = False 
            print(line.strip())


