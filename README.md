## SICAP TASKS

Proiectul include o serie de sarcini pentru analiza datelor din fișiere CSV ce conțin achiziții directe ale primăriilor. Acestea se fac folosind biblioteca [pandas](https://pandas.pydata.org/) pentru [Python 3.x](https://www.python.org). 

Pentru a utiliza proiectul, rulați următoarea comandă în terminal:
    
    pip install -r requirements.txt

Programul analizeaza, la momentul de față, urmatoarele fișiere:

- `achizitii_directe-primarii-2022.csv`
- `achizitii_directe-primarii-2021.csv`
- `achizitii_directe-primarii-2020.csv`

## Task 1

Scriptul Task1.py conține 2 subprograme: 
- `firme_unice` - returnează numărul de firme unice care au fost înregistrate pe e-licitatie.ro
- `most_used_cpv_codes` - returneaza primele 20 cele mai folosite coduri CPV 
