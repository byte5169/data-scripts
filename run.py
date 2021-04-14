import pandas as pd
from datascrpits import path
from datascrpits.preprocessing import DataConvert, DataFilter, DataCleaning
from datascrpits.visualize import DataVisualize
from datascrpits.processing import DataProcessing


def main():
    df = pd.read_csv('./data/covid_19_data.csv')

    d, t, v = DataProcessing(df).data_split()



if __name__ == '__main__':
    main()
