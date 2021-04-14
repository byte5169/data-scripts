from sklearn.model_selection import train_test_split
from datascrpits.preprocessing import RawData


class DataProcessing:
    """
    Class responsible for any type of basic data processing. \n
    Methods: \n
    data_split() - return three DataFrames with column converted to UNIX. \n

    :df: DataFrame to operate on. \n
    """

    def __init__(self, df):
        self.df = df

    def data_split(self, train_frac=0.8, random_state=42):
        """
        Randomly split dataset, based on these ratios:
            'train': train_frac
            'valid': (1-train_frac) / 2
            'test':  (1-train_frac) / 2

        :train_frac: ratio of train set to whole dataset

        Eg: passing train_frac=0.8 gives a 80% / 10% / 10% split
        """

        df_full = self.df

        assert train_frac >= 0 and train_frac <= 1, "Invalid training set fraction"

        X_train, X_tmp = train_test_split(
            df_full, train_size=train_frac, random_state=random_state)

        X_val, X_test = train_test_split(
            X_tmp, train_size=0.5, random_state=random_state)

        return X_train, X_val, X_test


class DataSentiment:
    pass


class DataTwitter:
    pass
