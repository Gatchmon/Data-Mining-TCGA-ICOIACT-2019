import os, csv
import pandas as pd
import numpy as np
from scipy import std
from scipy import nanstd

cancer_barcode = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
normal_barcode = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

data = pd.read_csv("COAD__miRNAExp__RPM.txt", delimiter='\t')
newdata = pd.DataFrame(data=data)
# print(newdata)

delete = []
header = list(newdata)
# for i in header:
#     if i[13:15] in normal_barcode:
#         delete.append(i)

for i in header:
    if i[13:15] in cancer_barcode:
        delete.append(i)

# print(newdata)

finaldata = newdata.drop(columns=delete)
print(finaldata)

# trimmed_data = pd.DataFrame(data=finaldata)
# print(trimmed_data[:2])


# print(list(trimmed_data))
# for i in list(trimmed_data):
#     print(i)

# for i in list(trimmed_data):
#     if i [13:15] in normal_barcode:
#         print(i)


finaldata.to_csv('normal_mirna.csv', sep=';')
#
#---------------------------------------------------------------------------------------------------------------#

# cancer_barcode = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
# normal_barcode = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
# bracket = []
# cancer_b = []
# normal_b = []
#
# with open('lihc_cancer_filtered.csv') as data:
#     a = csv.reader(data, delimiter=',')
#     for i in a:
#         bracket.append(i)
#         break
#
#
# #print(bracket)
# for i in bracket:
#     for j in i:
#         if j[13:15] in cancer_barcode:
#             cancer_b.append(j)
#         elif j[13:15] in normal_barcode:
#             normal_b.append(j)
#
# for i in cancer_b:
#     print(i)
#
# for i in normal_b:
#     print(i)








