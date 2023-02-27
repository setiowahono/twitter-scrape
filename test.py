import pandas as pd

df = pd.read_csv('tweet_@BANKBRI_ID_1000.csv', on_bad_lines='skip', delimiter=',')

print(df.head(100))