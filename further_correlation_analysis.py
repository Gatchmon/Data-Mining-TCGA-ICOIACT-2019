import pandas as pd

#-----------------------------------joining column of rho and p-values--------------------------------------------------

# mirup_genedown = pd.read_csv('pvalue_mirdown_geneup.txt', sep='\t',
#                                     names = ['mirna_id', 'gene_id', 'p_value'])
# rho_mirup_genedown = pd.read_csv('rho_mirdown_geneup.txt', sep='\t',
#                                  names = ['mirna_id', 'gene_id', 'rho_value'])
#
# rho_value = []
# for i in rho_mirup_genedown['rho_value']:
#     rho_value.append(i)
#
# mirup_genedown['rho_value'] = rho_value
#
# mirup_genedown.to_csv('mirdown_geneup.csv', sep=';')

#-------------------------------------------Finding truth--------------------------------------------------------------

mirup_genedown = pd.read_csv('mirup_genedown.csv', sep=';')
mirdown_geneup = pd.read_csv('mirdown_geneup.csv', sep=';')

data = mirup_genedown.dropna()

for index, rows in mirup_genedown.iterrows():
    if float(rows['p_value']) <= 0.05:
        if float(rows['rho_value']) < -0.5:
            print('Mirna ID: '+str(rows['mirna_id']))
            print('Gene ID: ' + str(rows['gene_id']))
            print('P Value: ' + str(rows['p_value']))
            print('Rho Value: ' + str(rows['rho_value']))