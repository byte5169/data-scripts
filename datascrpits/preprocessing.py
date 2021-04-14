from sklearn import preprocessing
import pandas as pd
import re


class RawData:
    """
    Class that stores CSV path \n
    self.df converts CSV to DataFrame
    """

    def __init__(self, df, path):
        self.df = df
        self.path = path

    def _gen_new_filename(self, func_name, df_to_save):
        """
        Private method to save temporary results in CSV /n
        :func_name: string that should contain main changes to file
        :df_to_save: DataFrame that has to be saved to CSV
        """

        try:
            new_location = f"{self.path}/{func_name}.csv"
            df_to_save.to_csv(new_location, mode="w+", index=False)
        except Exception:
            print("\nFile was not able to save. \n")


class DataFilter(RawData):
    """
    Class responsible for data filtration. \n
    Methods: \n
    drop_duplicates() - return a DataFrame without duplicated rows. \n
    filter_columns() - return a DataFrame with only specified columns. \n
    filter_content() - return a DataFrame cleaned from specified row values. \n

    :df: DataFrame to operate on. \n
    :path: path to folder where temporary results should be stored (Example: ./data/). \n
    """

    def __init__(self, df, path):
        super().__init__(df, path)

    def drop_duplicates(self):
        """
        :return: DataFrame
        """
        df_full = self.df
        df_no_dups = df_full.drop_duplicates()

        # print out result
        print(
            "Number of duplicated rows: \n",
            len(df_full) - len(df_no_dups.drop_duplicates()),
        )

        # save result to CSV
        self._gen_new_filename("drop_dups", df_no_dups)

        # return
        return df_no_dups

    def drop_columns(self, columns):
        """
        :columns: takes a column or a list of columns you want to drop in the DataFrame \n

        :return: DataFrame
        """
        df_full = self.df
        df_drop = df_full.drop(columns=columns, axis=1)

        # print out result
        print("Columns in the DataFrame:")
        for c in df_drop.columns:
            print(c)

        # save result to CSV
        self._gen_new_filename("drop_columns", df_drop)

        # return
        return df_drop

    def filter_columns(self, columns):
        """
        :columns: takes list of columns you want to leave in the DataFrame \n

        :return: DataFrame
        """
        df_full = self.df
        df_short = df_full[columns]

        # print out result
        print("Columns in the DataFrame:")
        for c in df_short.columns:
            print(c)

        # save result to CSV
        self._gen_new_filename("filter_columns", df_short)

        # return
        return df_short

    def filter_content(self, text, column):
        """
        :text: a number or a string that needs to be filtered out \n
        :column: take a column name you want to remove content from. \n

        :return: DataFrame
        """
        df_full = self.df

        try:
            # check if provided value is a number
            if type(text) == int or type(text) == float:
                df_removed = df_full[~df_full[column].isin([text])]

                print("Number of rows removed: \n",
                      len(df_full) - len(df_removed))

                # save result to CSV
                self._gen_new_filename("filter_content", df_removed)

                # return
                return df_removed
            # check if provided value is a string
            elif type(text) == str:
                removed_t = df_full[df_full[column].str.contains(
                    text, na=False)].index
                df_removed = df_full.drop(removed_t, axis=0)

                print("Number of rows removed: \n", len(removed_t))

                # save result to CSV
                self._gen_new_filename("filter_content", df_removed)

                # return
                return df_removed
            # check for anything else
            else:
                return "Please use a number or a string."
        except AttributeError:
            print(
                "Please use int/float/string value for respectfull DataFrame column type."
            )


class DataConvert(RawData):
    """
    Class responsible for any type of data convertions inside DataFrames. \n
    Methods: \n
    convert_to_unix() - return a DataFrame with column converted to UNIX. \n
    data_label() - return DataFrame with non-numerical column converted to numerical. /n

    :df: DataFrame to operate on. \n
    :path: path to folder where temporary results should be stored (Example: ./data/). \n
    """

    def __init__(self, df, path):
        super().__init__(df, path)

    def convert_to_unix(self, column, drop=False):
        """
        :column: takea a column name you want to convert to UNIX. \n
        :drop: set to True if you want to drop original column. False by default. \n 

        :return: DataFrame
        """
        df_full = self.df

        # convert column to datetime format
        df_full[f"{column}_UNIX_time"] = df_full[column].astype("datetime64")
        # convert to UNIX
        df_full[f"{column}_UNIX_time"] = df_full[f"{column}_UNIX_time"].apply(
            lambda row: (row - pd.Timestamp("1970-01-01")
                         ) // pd.Timedelta("1s")
        )

        # check if user want to drop original column
        if drop == True:
            df_full = df_full.drop(columns=column, axis=1)

            # save result to CSV
            self._gen_new_filename("to_unix", df_full)

            # print out result
            print(f"Column '{column}' was converted to UNIX and dropped.")

            # return
            return df_full
        else:
            # save result to CSV
            self._gen_new_filename("to_unix", df_full)

            # print out result
            print(f"Column '{column}' was converted to UNIX.")

            # return
            return df_full

    def data_label(self, column, map=True):
        """
        :column: takea a column name you want to label. \n
        :map: set to False if you don't want to save mappings. True by default. \n

        :return: DataFrame
        """

        print("MAY TAKE A WHILE... \n")
        df_full = self.df
        le = preprocessing.LabelEncoder()

        # creates a new column with numerical labels
        df_full[f'{column}_int'] = le.fit_transform(df_full[f'{column}'])

        # save mapping to a dict and to a txt
        le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))

        # print out result
        print(f"Column '{column}' was labeled. \n")

        # save mapping to 'mapping.txt'
        if map == True:
            f = open(f'{self.path}mapping.txt', 'w+')
            f.write(repr(le_name_mapping) + '\n')
            f.close()
            print(f"Mapping for '{column}' was saved at 'mapping.txt' \n")

        df_label = df_full.drop(columns=column, axis=1)

        # save result to CSV
        self._gen_new_filename("label", df_label)

        # return
        return df_label


class DataCleaning:
    """
    Class responsible for any type of data cleaning. \n
    Methods: \n
    clean_txt() - return a cleaned text string. \n

    :text: regex data cleaning out of hash tags, mentions, urls \n
    """

    def __init__(self, text):
        self.text = text

    def clean_txt(self):
        """
        :return: cleaned input as a string
        """

        text = self.text

        # removing @mentions
        text = re.sub("@[A-Za-z0–9]+", "", text)
        # removing '#' hash tag
        text = re.sub("#", "", text)
        # removing RT
        text = re.sub("RT[\s]+", "", text)
        # removing hyperlink
        text = re.sub("https?:\/\/\S+", "", text)

        return text
