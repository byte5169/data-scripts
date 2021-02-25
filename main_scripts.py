#####################################################
# Saving test vs predictions into csv
#####################################################
# df2 = pd.DataFrame(columns=['test_row', 'predicted_cat'])
# for i in range(len(X_test)):
# 	# print("X=%s, Predicted=%s" % (X_test.iloc[i], y_pred[i]))
#   df2 = df2.append({'test_row': X_test.iloc[i], 'predicted_cat': y_pred[i]}, ignore_index=True)
# df2.to_csv('preds.csv',mode='w+', index=False)


#####################################################
# Creating dummies
#####################################################
# from sklearn.preprocessing import LabelEncoder
#
# one_hot = pd.get_dummies(df['assignee'])
# df = df.drop('assignee', axis=1)
# df = df.join(one_hot)

#####################################################
# Labeling ALL non-numerical categories
#####################################################
#
# label_encoder = LabelEncoder()
# mappings = []
# for i, col in enumerate(df):
#     if df[col].dtype == 'object':
#         df[col] = label_encoder.fit_transform(np.array(df[col].astype(str)).reshape((-1,)))
#         mappings.append(dict(zip(label_encoder.classes_, range(1, len(label_encoder.classes_) + 1))))

##############################################################
# Labeling a single non-numerical category and getting mapping
##############################################################
# from sklearn import preprocessing
# le = preprocessing.LabelEncoder()
# df = pd.read_csv('///')
#
# # creates a new column with numerical labels
# df['category_int'] = le.fit_transform(df['category'])
# # save mapping to a dict and to a txt
# le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
#
# f = open('results/mapping.txt', 'w+')
# f.write(repr(le_name_mapping) + '\n')
# f.close()

#####################################################
# Finding URLs in DF, adding them to new csv
#####################################################

# df = pd.read_csv(r"D:\python data folder\project-1\export.csv")

# reg_exp = regex.compile(
#     r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](
# ?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af
# |ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch
# |ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf
# |gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km
# |kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz
# |na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg
# |sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy
# |uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([
# ^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[
# .\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel
# |travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw
# |by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk
# |fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je
# |jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr
# |ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs
# |ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt
# |tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
# )

# l = []
# for i, r in df.iterrows():
#     string = df["log"].loc[i]

#     if reg_exp.search(string):
#         string = string.strip()
#         l.append(string)

# df_en = pd.DataFrame(l, columns=["log"])
# df_en = df_en.drop_duplicates(subset="log").reset_index()
# df_en = df_en["log"]
# df_en.to_csv("log_en_url.csv", mode="w+", index=True, sep=",")

#####################################################
# Searching Cyrillic in list and removing from DF
#####################################################

# df = pd.read_csv(r"D:\python data folder\project-1\log_en.csv")
# alphabet_regular_expression = regex.compile("\p{Cyrillic}")
# l = []
# for i, r in df.iterrows():
#     string = df['log'].loc[i]

#     if alphabet_regular_expression.search(string):
#         print(string)
#     else:
#         string = string.strip()
#         l.append(string)
# df_en = pd.DataFrame(l, columns=['log'])
# df_en = df_en.drop_duplicates(subset='log').reset_index()
# df_en = df_en['log']
# df_en.to_csv('log_en_2.csv', mode="w+", index=True, sep=",")