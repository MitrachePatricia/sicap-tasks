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
    cpv_count = df['publicDirectAcquisition.cpvCode.localeKey'].value_counts().head(20)
    cpv_count = cpv_count.rename_axis("CPV Code").reset_index(name="De cate ori a aparut")
    cpv_count.index = cpv_count.index + 1
    print("\nCele mai folosite coduri CPV in " + file[year] + " sunt: \n")
    print(cpv_count)

most_used_cpv_codes('achizitii_directe-primarii-2022.csv')
most_used_cpv_codes('achizitii_directe-primarii-2021.csv')
most_used_cpv_codes('achizitii_directe-primarii-2020.csv')
