import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import itertools

data1 = pd.read_csv('cancer_gene.csv', delimiter=';')
data2 = pd.read_csv('cancer_mirna.csv', delimiter=';')

data_cancer_genes = data1.drop(columns='Unnamed: 0')
data_mirna_cancer = data2.drop(columns='Unnamed: 0')

cancer_genes = pd.DataFrame(data=data_cancer_genes)
mirna_cancer = pd.DataFrame(data=data_mirna_cancer)

column_cancer = []
column_mirna = []
deleted_column = []

counter = 0
counter1 = 0
counter2 = 0

for i in list(cancer_genes):
    counter += 1
    column_cancer.append(i)

for i in list(mirna_cancer):
    counter1 += 1
    column_mirna.append(i[:16])

for i in column_cancer:
    if i == 'gene_id':
        continue
    if i[:16] not in column_mirna:
        counter2 += 1
        deleted_column.append(i)

# for i in column_cancer:
#     print(i)
#
# for i in column_mirna:
#     print(i)
#
# for i in deleted_column:
#     print(i)

filtered_cancer_genes = cancer_genes.drop(columns=deleted_column)

# print(filtered_cancer_genes)
# print(mirna_cancer)

transposed_filtered_cancer_genes = filtered_cancer_genes.T
transposed_mirna_cancer = mirna_cancer.T

new_header = transposed_filtered_cancer_genes.iloc[0]
transposed_filtered_cancer_genes = transposed_filtered_cancer_genes[1:]
transposed_filtered_cancer_genes.columns = new_header

new_header2 = transposed_mirna_cancer.iloc[0]
transposed_mirna_cancer = transposed_mirna_cancer[1:]
transposed_mirna_cancer.columns = new_header2

df_genes = pd.DataFrame(data=transposed_filtered_cancer_genes)
df_mirna = pd.DataFrame(data=transposed_mirna_cancer)

value = []
counter = 0
for i in list(df_mirna):
    a = df_mirna[i]
    b = df_genes['A1BG']
    value.append(stats.pearsonr(a,b))
    counter += 1

# pearson1 = []
# pearson2 = []
# for i in value:
#     if i == 'nan':
#         continue
#     pearson1.append(i[0])
#     pearson2.append(i[1])

spearman = []
counter2 = 0
for i in list(df_mirna):
    a = df_mirna[i]
    b = df_genes['A1BG']
    spearman.append(stats.spearmanr(a,b))
    counter2 += 1

for i in spearman:
    print(i[1])

a = df_mirna['hsa-let-7a-1']
b = df_genes['A1BG']

print(stats.pearsonr(a, b))
print(stats.spearmanr(a, b))

plt.scatter(a, b, color=['green'])
plt.title('Pearson Correlation Between hsa-let-7a-1 and A1BG')
plt.xlabel('P-value of IQGAP1')
plt.ylabel('P-value of Each miRNAs')
plt.show()











