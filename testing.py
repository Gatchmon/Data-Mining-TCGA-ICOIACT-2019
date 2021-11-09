import pandas as pd

cancer_up = pd.read_csv('cancer_upregulation.csv', sep=';')
cancer_down = pd.read_csv('cancer_downregulation.csv', sep=';')
mirna_up = pd.read_csv('mirna_upregulation.csv', sep=';')
mirna_down = pd.read_csv('mirna_downregulation.csv', sep=';')

all_mirna = []

for i in list(mirna_up):
    all_mirna.append(i[:16])

deleted_column = []
for i in list(cancer_up):
    if i == 'gene_id':
        continue
    if i[:16] not in all_mirna:
        deleted_column.append(i)

cancer_up = cancer_up.drop(columns=deleted_column)
cancer_down = cancer_down.drop(columns=deleted_column)

# print(cancer_up)
# print(cancer_down)
print(mirna_up)
print(mirna_down)

# cancer_up.to_csv('cancer_up.csv', sep=';')
# cancer_down.to_csv('cancer_down.csv', sep=';')
# mirna_up.to_csv('mirna_up.csv', sep=';')
# mirna_down.to_csv('mirna_down.csv', sep=';')

