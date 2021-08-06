import pandas as pd
from datascrpits import path
from datascrpits.preprocessing import DataConvert, DataFilter, DataCleaning
from datascrpits.visualize import DataVisualize
from datascrpits.processing import DataProcessing


def main():
    df = pd.read_csv(
        './data/penguins_size.csv')

    DataVisualize(df).confusion_matrix("species", "island")


if __name__ == '__main__':
    main()
