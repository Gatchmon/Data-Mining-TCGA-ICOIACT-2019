import os, csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#---------------------------------NORMAL DATA HANDLING--------------------------------------------

data_normal = pd.read_csv("normal_gene.csv", delimiter=';')
normaldata = pd.DataFrame(data=data_normal)

drop1 = normaldata.drop(columns='Unnamed: 0')
new_normal_data = pd.DataFrame(data=drop1)


mean_normal = new_normal_data.mean(axis=1)
std = new_normal_data.std(axis=1, ddof=0)

average = []
for i in mean_normal:
    average.append(i)

stdev = []
for i in std:
    stdev.append(i)

stdev_two = []
for i in std:
    stdev_two.append(i*2)

drop_columns_tcga = []

new_normal_data['mean'] = average
new_normal_data['std'] = stdev
new_normal_data['std*2'] = stdev_two

for i in list(new_normal_data):
    if i[0:4] == 'TCGA':
        drop_columns_tcga.append(i)

normal_data_before_final = new_normal_data.drop(columns=drop_columns_tcga, axis=1)
normal_data_final = pd.DataFrame(data=normal_data_before_final)

# print(normal_data_final)

#-----------------------------------CANCER DATA HANDLING------------------------------------------------

data_cancer = pd.read_csv("cancer_gene.csv", delimiter=';')
cancerdata = pd.DataFrame(data=data_cancer)

drop = cancerdata.drop(columns='Unnamed: 0')
new_cancer_data = pd.DataFrame(data=drop)

mean_cancer = new_cancer_data.mean(axis=1)

average_cancer = []
for i in mean_cancer:
    average_cancer.append(i)

new_cancer_data['mean'] = average_cancer

drop_columns_tcga2 = []

for i in list(new_cancer_data):
    if i[0:4] == 'TCGA':
        drop_columns_tcga2.append(i)

cancer_data_before_final = new_cancer_data.drop(columns=drop_columns_tcga2, axis=1)
cancer_data_final = pd.DataFrame(data=cancer_data_before_final)
# print(cancer_data_final)

# print(cancer_data_before_final)

#------------------------------UPREGULATION - DOWNREGULATION - MODERATE DETERMINATION--------------------------

mean_two_times_std = []
mean_two_times_std_down = []
mean_two_times_std_sum = normal_data_final['mean'] + normal_data_final['std*2']
mean_two_times_std_down_sum = normal_data_final['mean'] - normal_data_final['std*2']

for i in mean_two_times_std_sum:
    mean_two_times_std.append(i)

for i in mean_two_times_std_down_sum:
    mean_two_times_std_down.append(i)

normal_data_final['mean+2*stdev'] = mean_two_times_std
normal_data_final['mean-2*stdev'] = mean_two_times_std_down

var1 = cancer_data_final['mean']
var2 = normal_data_final['mean+2*stdev']
var3 = normal_data_final['mean-2*stdev']
cancer_data_final['mean+2*stdev_normal'] = var2
cancer_data_final['mean-2*stdev_normal'] = var3
# print(cancer_data_final)

upregulation = cancer_data_final[cancer_data_final['mean'] > cancer_data_final['mean+2*stdev_normal']]
#upregulation --> mean+2*stdev_normal
downregulation = cancer_data_final[cancer_data_final['mean'] < cancer_data_final['mean+2*stdev_normal']]
#downregulation --> mean-2*stdev_normal
notexpressed = cancer_data_final[cancer_data_final['mean'] == cancer_data_final['mean+2*stdev_normal']]

# print(upregulation)
# print(downregulation)
# print(notexpressed)

cancer_gene_upregulation = 0
cancer_gene_downregulation = 0
cancer_gene_not_expressed = 0

for i in upregulation['gene_id']:
    cancer_gene_upregulation += 1

for i in downregulation['gene_id']:
    cancer_gene_downregulation += 1

for i in notexpressed['gene_id']:
    cancer_gene_not_expressed += 1

# print(cancer_gene_upregulation)
# print(cancer_gene_downregulation)
# print(cancer_gene_not_expressed)

#------------------------------------------APPOINT DEG TO NEW CSV FILE----------------------------------------

# print(new_cancer_data)
# print(downregulation)

selected_column = []
for i in upregulation['gene_id']:
    selected_column.append(i)

# print(selected_column)
transpose_gene = new_cancer_data.T
new_header = transpose_gene.iloc[0]
transpose_gene = transpose_gene[1:]
transpose_gene.columns = new_header

drop_column = []

for i in list(transpose_gene):
    if i not in selected_column:
        drop_column.append(i)

finaldata = transpose_gene.drop(columns=drop_column, axis=1)
finaldata = finaldata.T
finaldata = finaldata.drop(columns=['mean'], axis=1)
# print(finaldata)

finaldata.to_csv('cancer_upregulation.csv', sep=';')

#-------------------------------------------GENERATE PIE CHART-------------------------------------------------

# labels = ['Up Regulated Genes --> '+str(cancer_gene_upregulation),
#           'Down Regulated Genes --> '+str(cancer_gene_downregulation),
#           'Not Expressed Genes --> '+str(cancer_gene_not_expressed)]
# sizes = cancer_gene_upregulation, cancer_gene_downregulation, cancer_gene_not_expressed
#
# colors = ['aquamarine', 'lightblue', 'khaki']
#
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal')
# plt.title('Proportion of Genes Activity'+'\n'+'Total Genes Identified : '
#           +str(cancer_gene_upregulation+cancer_gene_downregulation+cancer_gene_not_expressed))
# plt.show()


