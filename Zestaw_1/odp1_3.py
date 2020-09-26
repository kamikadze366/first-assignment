import pandas as pd

df = pd.read_csv("./train.tsv", sep='\t', header=None)
dict = pd.read_csv("./description.csv", index_col=0, squeeze=True).to_dict()
df_description = df.iloc[:, [3]].replace(dict)  # Take only [3] column from df, all rows
df[len(df.columns)] = df_description
df.to_csv("Zestaw_1/out2.csv", index=False, header=False)