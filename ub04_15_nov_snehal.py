# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:51:29 2016

@author: snehalpatil
"""

import re 
import os
import sys 
import codecs
from os.path import basename
import pandas as pd
import string 
import time 
import collections
import pdb

path="/home/snehalpatil/Desktop/ub04/inputs recieved/txtOutput/11_txt_files"
filename=[]

for root,dirs,files in os.walk(path):
    if(len(files)>0):
        for file in files:
            filename.append(str(root)+os.sep+file)
dfr=pd.DataFrame([os.path.basename(val) for val in filename])

def birthdate(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("\d{8}",str(pa1))


        if len(dev3) > 0:
            dev4 = dev3[0]
        else:
            dev4 = " "
    except:
        dev4 = " "

    return dev4
    
def admission_date(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("\s\d{6}\s",str(pa1))


        if len(dev3) > 0:
            dev4 = dev3[0]
        else:
            dev4 = " "
    except:
        dev4 = " "

    return dev4


def patient_sex(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("[MF]",str(pa1))


        if len(dev3) > 0:
            dev4 = dev3[0]
        else:
            dev4 = " "
    except:
        dev4 = " "

    return dev4
    
def admission_hr(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("\s\d{6}\s.*\s\d{1}\s",str(pa1))
        dev4 = re.findall("\s\d{2}\s",str(dev3))

        if len(dev3) > 0:
            dev5 = dev4[0]
        else:
            dev5 = " "
    except:
        dev5 = " "

    return dev5

    
def admission_type(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("\s\d{6}\s.*\s\d{1}\s",str(pa1))
        dev4 = re.findall("\s\d{1}\s",str(dev3))

        if len(dev3) > 0:
            dev5 = dev4[0]
        else:
            dev5 = " "
    except:
        dev5 = " "

    return dev5
    
def admission_src(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("\s\d{6}\s.*\s\d{1}\s",str(pa1))
        dev4 = re.findall("\s\d{1}\s",str(dev3))

        if len(dev3) > 0:
            dev5 = dev4[1]
        else:
            dev5 = " "
    except:
        dev5 = " "

    return dev5
    
def admission_dhr(pa):
    try:
        pa1=pa[6:12]
        dev3 = re.findall("\s\d{1}\s.*\s\d{2}\s",str(pa1))
        dev4 = re.findall("\d{2}",str(dev3))

        if len(dev3) > 0:
            dev5 = dev4[0]
        else:
            dev5 = " "
    except:
        dev5 = " "

    return dev5
    
#def admission_stat(pa):
#    try:
#        pa1=pa[6:12]
#        dev3 = re.findall("\s\d{1}\s.*\s\d{2}\s",str(pa1))
#        dev4 = re.findall("\d{2}",str(dev3))
#
#        if len(dev3) > 0:
#            dev5 = dev4[1]
#        else:
#            dev5 = " "
#    except:
#        dev5 = " "
#
#    return dev5
#    
def pat_cntrl_no(pa):
    try:
        pa1=pa[0]
        dev4 = pa1[52:]

        if len(dev4) > 0:
            dev5 = dev4
        else:
            dev5 = re.findall("\d\w+",str(pa1))
    except:
        dev5 = " "

    return dev5
    
def med_rec_no(pa):
    try:
        pa1=pa[1]
        dev4 = pa1[108:125]

        if len(dev4) > 0:
            dev5 = dev4
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def type_bill(pa):
    try:
        pa1=pa[1]
        pa1 = pa1[108:]
        dev4 = re.findall("\s\d{4}",str(pa1))

        if len(dev4) > 0:
            dev5 = dev4[1]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def fed_tax_id(pa):
    try:
        pa1=pa[1:8]
        dev4 = re.findall("\s\d{9}\s",str(pa1))

        if len(dev4) > 0:
            dev5 = dev4
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def statement_frm(pa):
    try:
        pa1=pa[1:8]
        dev4 = re.findall("\s\d{9}\s.*",str(pa1))
        dev4 = re.findall("\s\d{6}\s",str(dev4))
        if len(dev4) > 0:
            dev5 = dev4[0]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def statement_to(pa):
    try:
        pa1=pa[1:8]
        dev4 = re.findall("\s\d{9}\s.*",str(pa1))
        dev4 = re.findall("\s\d{6}\s",str(dev4))
        if len(dev4) > 0:
            dev5 = dev4[1]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def patient_state(pa):
    try:
        pa1=pa[1:8]
        dev4 = re.findall("\s\d{6}\s.*[MF]",str(pa1))
        dev5 = re.findall("\s\d{6}\s.*\s\d{5}",str(dev4))
        dev6 = re.findall("\s\w{2}\s\s\s\d{5}?",str(dev5))
        if len(dev6) > 0:
            dev5 = re.findall("\s\w{2}\s",str(dev6))
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def patient_pincode(pa):
    try:
        pa1=pa[1:8]
        dev4 = re.findall("\s\d{6}\s.*[MF]",str(pa1))
        dev5 = re.findall("\s\d{6}\s.*\s\d{5}",str(dev4))
        dev6 = re.findall("\s\w{2}\s\s\s\d{5}?",str(dev5))
        if len(dev6) > 0:
            dev5 = re.findall("\s\w{5}",str(dev6))
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def tot_amt(pa):
    try:
        dev4 = re.findall("[1]\s{7}[1].*\s\s\s[Y]\s\s",str(pa))
        dev7 = re.findall("\d{6}\s.*\d{10}",str(dev4))
        r=dev7[0]
        dev=r.split()
        if len(dev4) > 0:
            dev5 = dev[1]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
     
    
def creation_date(pa):
    try:
        dev4 = re.findall("[1]\s{7}[1].*\s\s\s[Y]\s\s",str(pa))
        dev7 = re.findall("\d{6}\s",str(dev4))
        if len(dev4) > 0:
            dev5 = dev7
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
     
#    
def npi(pa):
    try:
        dev4 = re.findall("[1]\s{7}[1].*\s\s\s[Y]\s\s",str(pa))
        dev7 = re.findall("\d{10}",str(dev4))
        if len(dev4) > 0:
            dev5 = dev7
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def insureds_name(pa):
    try:
        dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\s\d{2,3}.*\s\s\d{2}\s",str(dev4))
        dev44 = re.findall("\s\Y\s.*",str(dev6))
        dev8 = re.findall(",.*,",str(dev44))
        dev88 = re.findall("'.*\d{2}",str(dev8))
        r=dev88[0]
        w=r.split()
        if len(dev4) > 0:
            dev5 = w[0]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def pat_rel(pa):##done
    try:
        dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\s\d{2,3}.*\s\s\d{2}\s",str(dev4))
        dev44 = re.findall("\s\Y\s.*",str(dev6))
        dev8 = re.findall("\s\d{2}\s",str(dev44))
        if len(dev4) > 0:
            dev5 = dev8
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
    
def rel_info(pa):##done
    try:
        dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\s\Y|N\s.*\s\s\s\d{2}\s",str(dev4))
        dev44 = re.findall("\s\Y|N\s",str(dev6))
        dev7=dev44[0]+","+dev44[2]
        if len(dev4) > 0:
            dev5 = dev7
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def ass_benfit(pa):##done
    try:
        dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\s\Y|N\s\s\s\Y|N.*\d{2}\s",str(dev4))
        dev44 = re.findall("\s\Y|N\s",str(dev6))
        dev7=dev44[1]+","+dev44[3]
        if len(dev4) > 0:
            dev5 = dev7
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5

    
def oth_prov_id(pa):##done
    try:
#        dev4 = re.findall("\s\Y\s.*",str(pa))
#        dev9 = re.findall("\s\Y\s.*\s\s\s\d{2}\s",str(dev4))
#        e=dev9[0]
#        w=e.split(',')
        dev3 = re.findall("\s\Y.*",str(pa))
        d=dev3[0]
        s=d.split(',')
        w=s[0]
        dev3 = re.findall("\w+",str(w))
        if len(dev4) > 0:
            dev5 = dev3[4]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
       
    
    
def atten_phy(pa):##done
    try:
        pa1=pa[20:]
        #dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\d{10}.*",str(pa1))
        dev44 = re.findall(",.*,",str(dev6))
        r=dev44[0]
        t=r.split(',')
        if len(dev4) > 0:
            dev5 = t[1]
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def atten_phy_npi(pa):##done
    try:
        pa1=pa[20:]
        #dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\d{10}",str(pa1))
       
        if len(dev4) > 0:
            dev5 = dev6
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    

def prior_payments(pa):##done
    try:
        dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\d+",str(dev4))
        dev7=dev6[0]+","+dev44[4]
        if len(dev4) > 0:
            dev5 = dev7
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
def amount_due(pa):##done
    try:
        dev4 = re.findall("\s\Y\s.*",str(pa))
        dev6 = re.findall("\d+",str(dev4))
        dev7=dev6[5]
        if len(dev4) > 0:
            dev5 = dev7
        else:
            dev5 = ""
    except:
        dev5 = " "

    return dev5
    
patient_birthdate=[]
date_admission=[]
patient_sex2=[]
admission_Hr=[]
admission_type2=[]
admission_src2=[]
admission_dhr2=[]
PatientCNTL_No=[]
Medical_Rcd_no=[]
Bill_type=[]
Fedtax=[]
Statement_from=[]
Statement_to=[]
patient_state2=[]
patient_zipcode2=[]
Total_amount=[]
creation_date2=[]
NPI=[]
Ins_name=[]
pat_relationship=[]
rel_info2=[]
Ass_benefits=[]
oth_prov_id2=[]
Operting_phy_name=[]
atten_phy_npi2=[]
prior_payments2=[]
amount_due2=[]
file_name=[]

for file in filename: 
#    IdNumber =[]
    #print file
    doc_str = codecs.open(file,"r", 'utf-8','ignore').read()
    d=doc_str.encode('utf-8')
    pat=re.sub("\r","",str(d))
    doc_str1 = re.sub("\n","",str(d))
    pa=string.split(pat, '\n') 
###########Calling all functions defined##########################3
    #print(file)
    birthdate1=birthdate(pa)
    admission_date1=admission_date(pa)
    patient_sex1=patient_sex(pa)
    admission_hr1=admission_hr(pa)
    admission_type1=admission_type(pa)
    admission_src1=admission_src(pa)
    admission_dhr1=admission_dhr(pa)
   
    pat_cntrl_no1=pat_cntrl_no(pa)
    med_rec_no1=med_rec_no(pa)
    type_bill1=type_bill(pa)
    fed_tax_id1=fed_tax_id(pa)
    statement_frm1=statement_frm(pa)
    statement_to1=statement_to(pa)
    patient_state1=patient_state(pa)
    patient_pincode1=patient_pincode(pa)
    tot_amt1=tot_amt(pa)
    creation_date1=creation_date(pa)
    npi1=npi(pa)
    insureds_name1=insureds_name(pa)
    pat_rel1=pat_rel(pa)
    rel_info1=rel_info(pa)
    ass_benfit1=ass_benfit(pa)
    oth_prov_id1=oth_prov_id(pa)
    atten_phy1=atten_phy(pa)
    prior_payments1=prior_payments(pa)
    amount_due1=amount_due(pa)
    atten_phy_npi1=atten_phy_npi(pa)

   
####Appending the values to the lists#############################
    patient_birthdate.append(birthdate1)
    date_admission.append(admission_date1)
    patient_sex2.append(patient_sex1)
    admission_Hr.append(admission_hr1)
    admission_type2.append(admission_type1)
    admission_src2.append(admission_src1)
    admission_dhr2.append(admission_dhr1)
    PatientCNTL_No.append(pat_cntrl_no1)
    Medical_Rcd_no.append(med_rec_no1)
    Bill_type.append(type_bill1)
    Fedtax.append(fed_tax_id1)
    Statement_from.append(statement_frm1)
    Statement_to.append(statement_to1)
    patient_state2.append(patient_state1)
    patient_zipcode2.append(patient_pincode1)
    Total_amount.append(tot_amt1)
    creation_date2.append(creation_date1)
    NPI.append(npi1)
    Ins_name.append(insureds_name1)
    pat_relationship.append(pat_rel1)
    rel_info2.append(rel_info1)
    Ass_benefits.append(ass_benfit1)
    oth_prov_id2.append(oth_prov_id1)
    Operting_phy_name.append(atten_phy1)
    atten_phy_npi2.append(atten_phy_npi1)
    amount_due2.append(amount_due1)
    prior_payments2.append(prior_payments1)
    file_name.append(os.path.basename(file))


#'admission_dhr':admission_dhr2,'patient_sex':patient_sex2,'prior_payments':prior_payments2,
#'amount_due':amount_due2,' oth_prov_id': oth_prov_id2,'rel_info':rel_info2,
#'atten_phy_npi':atten_phy_npi2,'creation_date':creation_date2,'Patient Zipcode':Pat_Zipcode2,
#'patient_state':patient_state2,'patient_sex':patient_sex2,'admission_type':admission_type2,"admission_src":admission_src2, 

    colnames = {'Patient DOB': patient_birthdate,'admission_dhr':admission_dhr2,  
'PatientCNTL_No':PatientCNTL_No,' Medical_Rcd_no': Medical_Rcd_no,'Bill_type':Bill_type,'Fedtax':Fedtax,'Statement_from':Statement_from,  
'Statement_to':Statement_to,'NPI':NPI,
'amount_due':amount_due2,' oth_prov_id': oth_prov_id2,'rel_info':rel_info2,
'patient_state':patient_state2,'patient_sex':patient_sex2,'admission_type':admission_type2,"admission_src":admission_src2, 
'atten_phy_npi':atten_phy_npi2,'creation_date':creation_date2,'Patient Zipcode': patient_zipcode2,
'Ass_benefits':Ass_benefits,'Operting_phy_name':Operting_phy_name,'admission_Hr':admission_Hr, 
'patient_sex':patient_sex2,'prior_payments':prior_payments2,'File Name':file_name,'date_admission':date_admission,
'Total_amount':Total_amount,'Ins_name':Ins_name,'pat_relationship':pat_relationship}

    columns = collections.OrderedDict(colnames)

    result = pd.DataFrame(columns)
#    result.replace("[","")  

#print Amountpaid
#print("--- %s seconds ---" % (time.time() - start_time))
result.to_csv("/home/snehalpatil/Desktop/ub04/inputs recieved/txtOutput/11_txt_files/to_test_UB0423.csv",sep='$')

    