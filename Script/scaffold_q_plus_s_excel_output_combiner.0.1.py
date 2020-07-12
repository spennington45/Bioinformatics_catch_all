'''
@author: Tyler Weirick
@date 2013-7-16
This is a program to combine output from scaffold q plus in various ways.
'''

from math import fsum
from sys import hexversion

#=============================================================================
#                                 Constants
#=============================================================================

MIN_VERSION = "0x30200f0"

#Enter the file names here. 
file1 = "AUY9221.txt"
file2 = "17DMAG.txt"


#=============================================================================
#                                 Functions
#=============================================================================


def outputtotsv(file_name,file_set,file_dict):
    """
    Output a the list contained as a value in a dict as a tsv file.
    names as the file name. 
    """
    output_list = []
    for key_el in file_set:
        output_list.append("\t".join(file_dict[key_el]))
    out_file = open(file_name,"w")
    out_file.write("\n".join(output_list))
    out_file.close()


def outputintersectiontotsv(file_name,file_set,file_dict1,file_dict2):
    """
    Output a the list contained as a value in a dict as a tsv file.
    names as the file name. 
    """
    output_list = []
    for key_el in file_set:
        output_list.append(key_el+"\t"+
            "\t".join(file_dict1[key_el])+"\t"+"\t"+"\t".join( file_dict2[key_el][1:] ) )
    out_file = open(file_name,"w")
    out_file.write("\n".join(output_list))
    out_file.close()
    

def average(ac_num,txt_list,illegal_str="No Values"):
    """
    This function averages the values from a list. Some of the elements may 
    contain the string "No Values" thus we will remove these before averageing
    the numerical values. If there are more "No Values" than normal values in 
    the list an average will not be preformed and "No Values" will be returned.
    If an average is done the float will be returned as a string. 
    """

    if illegal_str in txt_list:
        print("WARNING: ",txt_list.count(illegal_str),"found in ",ac_num)

    numbers_only_list = [x for x in txt_list if x != illegal_str]

    if float(len(numbers_only_list)) / float(len(txt_list)) > 0.5:

        sum_val = fsum([float(i) for i in numbers_only_list])

        return str( float(sum_val)/float(len(numbers_only_list)) )
    else:
        return illegal_str


def converttoplusorblank(pval,max_pval,average_value,average_cutoff):
    average_cutoff = float(average_cutoff)
    average_value = abs(float(average_value))
    pval = float(pval)
    max_pval = float(max_pval)

    if pval <= max_pval and average_value >= average_cutoff:
        return '"+"'
    else:
        return '"-"'


def exceltodict(file_name):
    """
    This function converts a tab delimited file output from scaffold q plus in the format

    #	Visible?	Starred?	Identified Proteins (2883/2903)	Accession Number	Molecular Weight
    Protein        Grouping Ambiguity	Mann Whitney Test (P-Value)
    Taxonomy	Quant 1	Quant 3	Quant 5	Quant 7	Quant 9	Quant 10	Quant 2	Quant 4	Quant 6	Quant 8

    RETURNS: 
    A dictionary with the accession values as the key and the value as a list of the values. 
    Identified Proteins (2883/2903)
    Accession Number    
    Mann Whitney Test (P-Value) 
    Quant 10 
    Quant 2 
    Quant 4 
    Quant 6 
    Quant 8      
    average(Quant 10,Quant 2,Quant 4,Quant 6,Quant 8)
    """
    illegal_str="No Values"
    prot_dict = {}
    start_reading = True
    max_pval = 0.05
    for line in open(file_name,'r'):
        if "END OF FILE" in line:
            start_reading = False

        if start_reading:
            split_line = line.strip().split("\t")
            if not split_line[4] in prot_dict:
            
                val_list = split_line[14:19]
                
                #Will be a space or float as an str
                avg_val_str = average(split_line[4],val_list,illegal_str)
                p_val = float(split_line[7].split("(")[-1].split("<")[-1].strip(")"))

                if avg_val_str == illegal_str:
                    significance = illegal_str
                else:
                    significance = converttoplusorblank(p_val,0.05,avg_val_str,0.6)
                
                p_val = str(p_val)
                

                CI = str(float(split_line[7].split("%")[0])/100.0)
                #3,4, 14-18, average of 14-18
                prot_dict.update(
                {
                split_line[4]:[
                    split_line[3], #Identified Proteins i.e. prot_name
                    CI,    #Confidence Interval
                    p_val, #P-Value
                    ]+
                    split_line[14:19] + 
                    [
                     avg_val_str, #Average
                     significance #Significance
                    ]    
                }
                )
            else:
                print("ERROR: all rows should be unique.")

    return prot_dict


#=============================================================================
#                                 Main Program
#=============================================================================

#Get dictionaries with acs as keys and desired values as values.
file_dict1 = exceltodict(file1)
file_dict2 = exceltodict(file2)


print("Number of entries in",file1+":",len(file_dict1))
print("Number of entries in",file2+":",len(file_dict2))
#Generate sets of acs
set1 = set(file_dict1.keys())
set2 = set(file_dict2.keys())


#Get the overlapping acs 
intersetion_of_files = set1 & set2
print("Number of overlapping entries between",file1,"and",file2+":",len(intersetion_of_files))
file_name = file1.strip(".txt")+"_"+file2.strip(".txt")+"intersection.txt"
outputintersectiontotsv(file_name,intersetion_of_files,file_dict1,file_dict2)


unique_to_file1 = set1 - set2
print("Number of unique entries in",file1,":",len(unique_to_file1))
file_name = file1.strip(".txt")+"_disjoint"+file2.strip(".txt")+".txt"
outputtotsv(file_name,unique_to_file1,file_dict1)


unique_to_file2 = set2 - set1
print("Number of unique entries in",file2,":",len(unique_to_file2))
file_name = file2.strip(".txt")+"_disjoint"+file1.strip(".txt")+".txt"
outputtotsv(file_name,unique_to_file2,file_dict2)




"""
convertpvaluestoplusorblank(
    max_pval,
    float(split_line[7].split("(")[-1].split("<")[-1].strip(")"))
),
"""