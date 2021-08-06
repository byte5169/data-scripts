import wordcloud
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")


class DataVisualize:
    """
    Class responsible for data visualization. \n
    Methods: \n
    word_cloud_image() - method that creates WordCloud image based on input dataframe column \n
    confusion_matrix() - method to make confusion matrix \n

    :df: DataFrame to operate on. \n
    """

    def __init__(self, df):
        self.df = df

    def word_cloud_image(self, column_name, image_name="wordcloud.png"):
        """
        :column_name: column to convert to wrod clood \n
        :image_name: path where to save image, for ex "data/wordcloud.png" \n
        """

        df_full = self.df

        # drop missing data
        df_full = df_full.dropna(subset=[column_name])

        # generate wordcloud
        words = " ".join([txt for txt in df_full[column_name]])
        cloud = wordcloud.WordCloud(
            width=500, height=300, random_state=21, max_font_size=110
        ).generate(words)
        plt.imshow(cloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig(image_name)

        print(f"Wordcloud image was saved as {image_name}")

    def confusion_matrix(self, column_name1, column_name2):
        """
        :column_name: name of two categorical columns to make confusion matrix
        """

        df_full = self.df

        # generate confusion matrix
        print(
            df_full
            .groupby([column_name1, column_name2])
            .size()
            .unstack(fill_value=0)
        )
