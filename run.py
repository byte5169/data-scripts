import pandas as pd
from datascrpits import path
from datascrpits.preprocessing import DataConvert, DataFilter

df = pd.read_csv('./data/covid_19_data.csv')

d = DataConvert(df, path)
d2 = d.data_label("Country/Region", map=True)

print(d2)
