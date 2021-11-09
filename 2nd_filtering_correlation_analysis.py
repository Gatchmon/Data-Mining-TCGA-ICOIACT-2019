import pandas as pd

fil_mirup_genedown  = pd.read_csv('filtered_mirup_genedown.csv', sep=';')
fil_mirdown_geneup = pd.read_csv('filtered_mirdown_geneup.csv', sep=';')

fil_mirup_genedown.sort_values(by=['rho_value'], inplace=True)
fil_mirdown_geneup.sort_values(by=['rho_value'], inplace=True)

drop = ['Unnamed: 0']
fil_mirup_genedown = fil_mirup_genedown.drop(columns=drop)
fil_mirdown_geneup = fil_mirdown_geneup.drop(columns=drop)

data = []
c = 0
for index, rows in fil_mirdown_geneup.iterrows():
    if c < 10:
        dict = {'mirna_id': rows['mirna_id'], 'gene_id': rows['gene_id'], 'p_value' :rows['p_value'],'rho_value':rows['rho_value']}
        data.append(dict)
        c += 1
    else:
        break

df = pd.DataFrame(data)
print(df)

df.to_csv('top10_mirdown_geneup.csv', sep=';')
