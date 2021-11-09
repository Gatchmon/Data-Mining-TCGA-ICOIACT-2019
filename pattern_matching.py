import os, csv

dtcga = [] #patientID complete
fdtcga = [] #patientID identifier
full = []

with open('coad_dataset.csv') as data:
    a = csv.reader(data, delimiter=',')
    for i in a:
        dtcga.append(i[34].strip())

dtcga.pop(0)

for i in dtcga:
    fdtcga.append(i[0:16])

for i in dtcga:
    full.append(i[:16])

print(fdtcga)
# print(dtcga)

cancer_barcode = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
normal_barcode = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

cancer = []
normal = []

for i in fdtcga:
    if i[13:15] in cancer_barcode:
        cancer.append(i)
    elif i[13:15] in normal_barcode:
        normal.append(i)

#FOR CANCER AND NORMAL TCGA BARCODE FOR RSTUDIO

# count_cancer = 0
# for i in cancer:
#      # print(i)
#      count_cancer += 1
# print('Total Cancer Genes: ' + str(count_cancer))
#
# count_normal = 0
# for i in normal:
#      # print(i)
#      count_normal += 1
# print('Total Normal Genes: ' + str(count_normal))
#
# print('Total Normal + Cancer : ' + str((int(count_cancer)+int(count_normal))))
# #

#-----------------------------------------------------------------------------------------------










