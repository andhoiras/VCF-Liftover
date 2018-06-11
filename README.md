# VCF-Liftover

Python script that creates shell scripts for parallel computing. The shell scripts merge VCF files from merge_file.txt and subsequently lifts them from one human genome (hg) build to another hg build e.g. hg38 to hg19.    

Folders and paths have to be inputted by the user. 

During the shell script run multiple temp files will be written. 

Dependencies:
- merge_file.txt: a line separated text file with a list of VCF files that will be merged.
- bcftools: for this script version 1.6 is used. 
- UCSC liftOver tool. It has to be present in the same folder as the VCF files. 



