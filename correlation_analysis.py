import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

cancer_up = pd.read_csv('cancer_upregulation.csv', sep=';')
cancer_down = pd.read_csv('cancer_downregulation.csv', sep=';')
mirna_up = pd.read_csv('mirna_upregulation.csv', sep=';')
mirna_down = pd.read_csv('mirna_downregulation.csv', sep=';')


# ------------------------------------USE THIS FOR THE MIRNA-------------------------------------------------------------

mirna_name = []
for i in mirna_up.iloc[:,0]:
    mirna_name.append(i)

#--------------------------ADJUSTMENT OF COLUMN BETWEEN CANCER_UP AND MIRNA_DOWN ---------------------------------------

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

#--------------------------------------ADJUSTING HEADER------------------------------------------------------------

cancer_up = cancer_up.T
new_header2 = cancer_up.iloc[0]
cancer_up = cancer_up[1:]
cancer_up.columns = new_header2

cancer_down = cancer_down.T
new_header2 = cancer_down.iloc[0]
cancer_down = cancer_down[1:]
cancer_down.columns = new_header2

mirna_up = mirna_up.T
new_header2 = mirna_up.iloc[0]
mirna_up = mirna_up[1:]
mirna_up.columns = new_header2

mirna_down = mirna_down.T
new_header2 = mirna_down.iloc[0]
mirna_down = mirna_down[1:]
mirna_down.columns = new_header2

# g_up = pd.DataFrame(data=cancer_up)
# g_down = pd.DataFrame(data=cancer_down)
# m_up = pd.DataFrame(data=mirna_up)
# m_down = pd.DataFrame(data=mirna_down)

# ----------------------------CORRELATION ANALYSIS--------------------------------------------------------------------
spearman = []
for i in list(mirna_up):
    a = mirna_up[i]
    b = cancer_down['HAND2']
    spearman.append(stats.spearmanr(a,b))

corr = []
pvalue = []
for i in spearman:
    corr.append(i[0])
    pvalue.append(i[1])

# print(corr)
# print(pvalue)

mirna_up = mirna_up.T
cancer_down = cancer_down.T

mirna_up['corr_with_genes'] = corr
mirna_up['pvalue_with_genes'] = pvalue

corr_note = []
pvalue_note = []

for i in mirna_up['pvalue_with_genes']:
    if i < 0.05:
        pvalue_note.append('Significant')
    elif i > 0:
        pvalue_note.append('-')

mirna_up['pvalue_notes'] = pvalue_note
mirna_up['mirna_name'] = mirna_name

# for index, row in mirna_up.iterrows():
#     if row['pvalue_with_genes']<= 0.05:
#         print('miRNAs Name: '+str(row['mirna_name']))
#         print('Corr Value: '+ str(row['corr_with_genes']))
#         print('P_Value: '+ str(row['pvalue_with_genes']))
#         print('Pvalue notes: '+ str(row['pvalue_notes']))
#         print('\n')

# data = mirna_up[['corr_with_genes', 'pvalue_with_genes', 'pvalue_notes']]
# print(data)

#-----------------------------------------DATA TESTING------------------------------------------------------------------

drop_column = ['corr_with_genes', 'pvalue_with_genes', 'pvalue_notes', 'mirna_name']
mirna_up = mirna_up.drop(columns=drop_column)

mirna_up = mirna_up.T
cancer_down = cancer_down.T

a = cancer_down['HAND2']
b = mirna_up['hsa-mir-200a']
# c = mirna_up['hsa-mir-708']
# d = mirna_up['hsa-mir-103a-2']

# print(mirna_up)
# print(cancer_down)

plt.scatter(a, b, color=['green'])
# plt.scatter(a, c, color=['blue'])
# plt.scatter(a, d, color=['red'])
plt.title('Scatterplot of hsa-mir-200a and HAND2')
plt.xlabel('Expression Value of miRNAs')
plt.ylabel('Expression Value of Genes')
plt.show()

# sns.regplot(x="Expression Value of miRNAs", y="Expression Value of Genes", data=[a,b])STX10