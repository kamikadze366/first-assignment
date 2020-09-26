import pandas as pd
# Text won't be truncated + all columns displayed
pd.set_option('display.width', None)  # No text wrapping
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Define columns names + which column to display
df = pd.read_csv("Zestaw_1/train.tsv", sep='\t', header=None)
df.columns = ["Cena w tys.", "Pokoje", "Powierzchnia", "Pietro", "Lokalizacja", "Opis"]  # Defining columns headers
res1 = df[['Pietro']]
res2 = df[["Cena w tys.", "Powierzchnia", "Opis"]].head()

print(res1, res2, df.info, sep='\n')
