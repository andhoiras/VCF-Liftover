


import pandas

import glob
import os
import fnmatch

#list_of_files = glob.glob("/home/people/andras/Data/VCF/VCF_files/./*.vcf") # creating list of all .txt files in current directory
list_of_files = os.listdir("/home/people/andras/Data/VCF/VCF_files/VCF_filtered/bgzip/Ped_fam_affec_noaffec")  


pattern = "*.txt"  


os.mkdir("QSUB_bcftools")
#os.mkdir("/home/people/andras/Data/VCF/VCF_files/VCF_filtered/bgzip/merge_files")
#os.mkdir("/home/people/andras/Data/VCF/VCF_files/VCF_filtered")

for file_name in list_of_files:  
	if fnmatch.fnmatch(file_name, pattern):

		Type = file_name.split(".") # splitting file_name separated by "."
		x = Type[0] # selecting first part of name
		z = x.split("_")  #splitting file_name separated by "_"
		p = z[0] # selecting first word of name
		y = p.replace("/", "")
		#os.chdir("/home/people/andras/Data/VCF/VCF_files/VCF_filtered/bgzip/Ped_fam_affec_noaffec")
		#df = pandas.read_csv(file_name, sep='\t', lineterminator='\n', keep_default_na=True, dtype = "object") # importing file with the name "file_name"	

		#df["End"] = ".vcf.gz"
		#df2 = df["merge"] = df[["Decode_ID", "End"]].apply(lambda x: ''.join(x), axis=1)
		
		#os.chdir("/home/people/andras/Data/VCF/VCF_files/VCF_filtered/bgzip/merge_files")
		#df2.to_csv(file_name.replace("txt" , "merge_file.txt"), sep="\t", index=False, na_rep="NA", header=False) # exporting file with
		#s.chdir("/home/people/andras")

		FO = open("QSUB_bcftools/"+ y + ".qsub",'w') #new file created 
		FO.write("#!/bin/sh \n")
		
		FO.write("\n")
		FO.write("module load bcftools/1.6 \n")
		FO.write("\n")
		FO.write("\n")
		FO.write("cd /home/people/andras/Data/VCF/VCF_files/VCF_filtered/bgzip \n")
		
		
		FO.write("\n")
		FO.write("bcftools merge -l merge_files/" +  y  + ".merge_file.txt -O v -o  " + y + ".vcf \n")
		FO.write("\n")
		FO.write("sed 's/\.\/\./0\/0/g' " + y + ".vcf > " + y + ".sed.vcf \n")
		FO.write("\n")

		FO.write("grep ^# " + y + ".sed.vcf > " + y + ".sed.header.vcf \n")

		FO.write("\n")
		
		FO.write("grep -v ^# " + y + ".sed.vcf | awk '{print $1, $2-1, $2,$3\"|\"$4\"|\"$5\"|\"$6\"|\"$7\"|\"$8\"|\"$9\"|\"$10\"|\"$11\"|\"$12\"|\"$13\"|\"$14\"|\"$15\"|\"$16\"|\"$17\"|\"$18\"|\"$19\"|\"$20\"|\"$21\"|\"$22}' > " + y + ".sed.bed \n")
		FO.write("\n")

		FO.write("sed -e 's/ [ ]*/\\t/g' " + y + ".sed.bed > " + y + ".sed.sed.bed \n")

		FO.write("\n")

		FO.write("./liftOver " + y + ".sed.sed.bed /home/people/andras/Data/VCF/VCF_files/VCF_filtered/merge/hg38ToHg19.over.chain.gz " + y + ".sed.sed.hg19.bed " + y + ".sed.sed.unlifted.bed \n")

		FO.write("\n")	


		FO.write("awk '{print $1, $3, $4}' " + y + ".sed.sed.hg19.bed | sed -e 's/|/\\t/g' | sed 's/  */\\t/g' > "+ y + ".sed.sed.hg19.sed.vcf \n")

		FO.write("\n")	
		FO.write("cat " + y + ".sed.header.vcf " + y + ".sed.sed.hg19.sed.vcf > " + y + "hg19.vcf \n")
		FO.write("\n")	

		FO.close()





