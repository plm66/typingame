import pandas as pd

#example web-hosted dataset

path='https://data.noteable.io/2015.csv'

happiness_df = pd.read_csv(path)

print(happiness_df)

