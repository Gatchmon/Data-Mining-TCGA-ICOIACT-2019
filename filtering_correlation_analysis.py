import pandas as pd

mirup_genedown = pd.read_csv('mirup_genedown.csv', sep=';')
mirdown_geneup = pd.read_csv('mirdown_geneup.csv', sep=';')

drop = ['no']
mirup_genedown = mirup_genedown.drop(columns=drop)
mirdown_geneup = mirdown_geneup.drop(columns=drop)

# print(mirup_genedown)
# print(mirdown_geneup)

l= []

for index, rows in mirdown_geneup.iterrows():
         if float(rows['p_value']) < 0.05:
            if float(rows['rho_value']) < -0.5:
                dict = {'mirna_id': rows['mirna_id'], 'gene_id': rows['gene_id'], 'p_value' :rows['p_value'],'rho_value':rows['rho_value']}
                l.append(dict)
                # new_gene.append(str(rows['gene_id']))
                # new_pvalue.append(rows['p_value'])
                # new_rho.append(rows['rho_value'])

                # print("Mirna ID : "+str(rows['mirna_id']))
                # print("Gene ID : "+str(rows['gene_id']))
                # print("P Value : "+str(rows['p_value']))
                # print("Rho Value : "+str(rows['rho_value']))
                # print('\n')

df = pd.DataFrame(l)
df.to_csv('filtered_mirdown_geneup.csv', sep=';')