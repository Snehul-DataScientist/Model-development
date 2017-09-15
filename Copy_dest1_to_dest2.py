# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:57:16 2017

@author: snehalpatil
"""

import os
import sys
import pdb
import shutil


####Assumption here Destination is a parent folder which has folders, 
##########This folders again have sub folders, We need to copy files 
################from this subfolders to Destination folder#########
#######InputDest= Parentfolder>folder>sub-folder>files
#####OutDest=Folder
############This code is to copy files from one destination to another#################
if __name__ == '__main__':
    mypath = "/home/snehalpatil/Desktop"
        
    Ocrpath = '/home/snehalpatil/Desktop/dir1/Output_Format_1 (copy)'
    Out_dir_path = mypath + '/ANCESTORY/I3_input_FILES2/All_json'

    
  
    folders = [ name for name in os.listdir(Ocrpath) if os.path.isdir(os.path.join(Ocrpath, name)) ]


    for fldr in folders: 
        IN_dir_path = os.path.join(Ocrpath,fldr)        
        OUT_dir_path = os.path.join(Out_dir_path) 
        file_copy(IN_dir_path, OUT_dir_path)                                        


##################Copy json Files from one destination to another############################

def file_copy(IN_dir_path, OUT_dir_path):
    jsonFiles = []
    subfolders = os.listdir(IN_dir_path)
    for sub2 in subfolders:
        IN_dir_path2 = os.path.join(IN_dir_path,sub2)
        filenames = os.listdir(IN_dir_path2)
        for name in [fi for fi in filenames if fi.endswith("FR_orgimage.json")]:
            jsonFiles.append(os.path.join(IN_dir_path2, name)) 
        for filen in jsonFiles:
            shutil.copy(filen, OUT_dir_path)
            shutil.move(os.path.join(OUT_dir_path,os.path.basename(filen)), os.path.join(OUT_dir_path,os.path.basename(filen).split("_FR")[0]+"FR_orgimage.json"))
    return
  
        
        
        
        