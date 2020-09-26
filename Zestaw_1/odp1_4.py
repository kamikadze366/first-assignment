import pandas as pd
import matplotlib.pyplot as plt

chosen_cols = ['Age', 'SurveyEase', 'CompTotal']
df = pd.read_csv("./survey_results_public.csv", usecols=chosen_cols).dropna()

# sort out invalid data
df = df[(df['Age'] > float(15)) & (df['Age'] < float(90)) & (df['CompTotal'] < 5e8)]
df.sort_values(by=chosen_cols, inplace=True)
print(df.head())

# renumber index
df.reset_index(drop=True, inplace=True)

# answers for grouping
answers = df.SurveyEase.unique()

for answer in answers:
    # data frame of valid values - filter
    x_val = df[df['SurveyEase'] == answer]
    # plot
    plt.plot(x_val['Age'], x_val['CompTotal'], 'gs', markersize=2)
    plt.xlabel('Age')
    plt.ylabel('Total compensation')
    plt.title('Survey difficulty: ' + answer)
    plt.show()