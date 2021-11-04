import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Les inn fil
df = pd.read_csv('./inputs/random_1000_results.csv')
# Erstatt tom string '' med NaN
df = df.replace(r'^\s*$', np.nan, regex=True)
#Kolonne-navnene: ['   n', ' insertion_cmp', ' insertion_swaps', ' insertion_time',' quick_cmp', ' quick_swaps', ' quick_time', ' merge_cmp',' merge_swaps', ' merge_time', ' selection_cmp', ' selection_swaps',' selection_time']
# print(df.columns)
#Konverter ikkenumerisk til float 
df[' insertion_cmp']=df[' insertion_cmp'].astype(float)
df[' insertion_swaps']=df[' insertion_swaps'].astype(float)
df[' insertion_time']=df[' insertion_time'].astype(float)
df[' selection_cmp']=df[ ' selection_cmp'].astype(float)
df[' selection_swaps']=df[' selection_swaps'].astype(float)
df[' selection_time']=df[' selection_time'].astype(float)

#plot med n på x-aksen, og øvrige på y
df.plot(x="   n", y=[' insertion_time',' selection_time',' quick_time',' merge_time'])

# Vis plottet
plt.show()