import pandas as pd
import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
data_dir = os.path.join(script_dir, 'data')
os.chdir(script_dir)

# cate firme unice sunt?
def firme_unice(file):
    file_path = os.path.join(data_dir, file)
    df = pd.read_csv(file_path, header=0)
    year = slice(-8, -4)
    print("Numarul de firme unice in " + file[year] + " este " + str(df['authority.entityId'].nunique()))

firme_unice('achizitii_directe-primarii-2022.csv')
firme_unice('achizitii_directe-primarii-2021.csv')
firme_unice('achizitii_directe-primarii-2020.csv')

# top 20 cele mai folosite coduri cpv
def most_used_cpv_codes(file):
    file_path = os.path.join(data_dir, file)
    df = pd.read_csv(file_path, header=0)
    year = slice(-8, -4)

    # extragere top 20 coduri CPV
    cpv_count = df['publicDirectAcquisition.cpvCode.localeKey'].value_counts().head(20)
    cpv_count = cpv_count.rename_axis("CPV Code").reset_index(name="Count")

    # extragere descrieri top 20 coduri CPV
    cpv_descriptions = df[['publicDirectAcquisition.cpvCode.localeKey', 'publicDirectAcquisition.cpvCode.text']].drop_duplicates()
    cpv_descriptions = cpv_descriptions.rename(columns={'publicDirectAcquisition.cpvCode.localeKey': 'CPV Code', 'publicDirectAcquisition.cpvCode.text': 'Description'})
    
    # combinare numarul de aparitii cu descrierea codulurilor cpv
    cpv_count = cpv_count.merge(cpv_descriptions)

    # adaugare coloana cu valoarea totala a contractelor pentru fiecare cod cpv
    cpv_total_value = df.groupby('publicDirectAcquisition.cpvCode.localeKey')['item.estimatedValueRon'].sum().reset_index()
    cpv_total_value = cpv_total_value.rename(columns={'publicDirectAcquisition.cpvCode.localeKey': 'CPV Code', 'item.estimatedValueRon': 'Total Value (in Ron)'})
   
    # formatarea coloanei de total value ca sa fie mai usor de citit (?)
    # cpv_total_value['Total Value (in Ron)'] = cpv_total_value['Total Value (in Ron)'].str.replace(',', '').astype('float64')
    # cpv_total_value['Total Value (in Ron)'] = cpv_total_value['Total Value (in Ron)'].apply(lambda x: '{:,.2f}'.format(x))

    # combinare numarul de aparitii cu valoarea totala a contractelor
    cpv_count = cpv_count.merge(cpv_total_value)
    
    # modificare index (ca sa inceapa de la 1 in loc de 0)
    cpv_count.index = cpv_count.index + 1
  
    print("\nCele mai folosite coduri CPV in " + file[year] + " sunt: \n")
    print(cpv_count)

most_used_cpv_codes('achizitii_directe-primarii-2022.csv')
most_used_cpv_codes('achizitii_directe-primarii-2021.csv')
most_used_cpv_codes('achizitii_directe-primarii-2020.csv')
