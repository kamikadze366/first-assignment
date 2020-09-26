import pandas as pd
df = pd.read_csv("./train.tsv", sep='\t', header=None)

# Average flat price
avg = "{:.0f}".format(df[0].mean())
df_avg = pd.DataFrame({avg})
df_avg.to_csv("Zestaw_1/out0.csv", index=False, header=False)

# Add SQM price column
df[len(df.columns)] = df[0]/df[2]

# Multifilter criteria
match = df[(df[1] >= 3) & (df[6] < df[6].mean())]
match[[1, 0, 6]].to_csv("Zestaw_1/out1.csv", index=False, header=False)