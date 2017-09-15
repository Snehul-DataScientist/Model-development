# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:50:49 2017

@author: snehalpatil
"""

###Code for searching specific extension files within folders##########

import re
import os
import codecs
import csv
import pandas as pd

if __name__ == '__main__':
    mypath = "/home/snehalpatil/Desktop"
        
    Ocrpath = '/home/snehalpatil/Desktop/FORGO/OCR'

    folders = [ name for name in os.listdir(Ocrpath) if os.path.isdir(os.path.join(Ocrpath, name)) ]
    
    for fldr in folders: 
        IN_dir_path = os.path.join(Ocrpath,fldr)  
        filenames = os.listdir(IN_dir_path)
        for name in [fi for fi in filenames if fi.endswith(".TXT.raw.txt")]:
            txtFiles.append(os.path.join(IN_dir_path, name)) 
    print (len(txtFiles))