import os, csv
import pandas as pd

data1 = pd.read_csv('coad_cancer.csv', delimiter=';')
data2 = pd.read_csv('mirna_cancer.csv', delimiter=';')
data_cancer_genes = data1.drop(columns='Unnamed: 0')
data_mirna_cancer = data2.drop(columns='Unnamed: 0')

# print(data_cancer_genes)
# print(data_mirna_cancer)

data_cancer = []
data_mirna = []

for i in list(data_cancer_genes):
    if i == 'gene_id':
        continue
    data_cancer.append(i[0:16])

for i in list(data_mirna_cancer):
    if i == 'GeneSymbol':
        continue
    data_mirna.append(i[0:16])

# for i in data_mirna:
#     print(i)

cancer_strange = []

for i in data_cancer:
    if i[0:16] not in data_mirna:
        cancer_strange.append(i)

print(cancer_strange)

# for i in data_cancer:
#     print(i[0:16])
#
# for i in data_mirna:
#     print(i[0:16])


# datacancer = pd.DataFrame(data=data_cancer)
# print(datacancer)

# datamirna = pd.DataFrame(data=data_mirna)
# print(datamirna)

