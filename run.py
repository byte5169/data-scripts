import pandas as pd
from datascrpits import path
from datascrpits.preprocessing import DataConvert, DataFilter, DataCleaning
from datascrpits.visualize import DataVisualize


def main():
    df = pd.read_csv('./data/covid_19_data.csv')

    d = DataCleaning(
        ['@ton дурачок посмотри лучше сюда http://url.net', '@ton дурачок посмотри лучше сюда http://url.net']).clean_txt()
    print(d)


if __name__ == '__main__':
    main()
