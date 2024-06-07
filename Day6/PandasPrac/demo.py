import numpy as np
import pandas as pd

data = {
    "name": ["Aakash", "Bhavesh", "Umit"],
    "city": ["Surat", "Baroda", "Una"],
    "salary": [12000, 15000, 16000],
}
df = pd.DataFrame(data)
new_df = pd.read_csv("Day6/PandasPrac/demo.csv")

# print("-" * 35)

new_df.index = ["first", "second", "third", "fourth"]  # type: ignore

# print(new_df.head(2))

# df.to_csv("data.csv", index=False)
# print(df.describe())

me_series = pd.Series(np.random.rand(20))
# print(me_series)

me_frame = pd.DataFrame(np.random.rand(334, 5), np.arange(334))

# print(me_frame.head(5))
# print(me_frame.describe())
# print(me_frame.dtypes)
# print(me_frame.index)
# print(me_frame.columns)

# ! 0 means row and 1 means column in NumPy

# ? print(me_frame.sort_index(axis=0, ascending=False).head())

# print(me_frame.head())

me_frame.columns = list("ABCDE")

# me_frame.loc[0]["B"] = 10.6638858

me_frame = me_frame.drop("E", axis=1)

# print(me_frame.head())

# * to get specific range of data from data frame we can write row index and column name in loc fn

# print(me_frame.loc[[0, 1], ["B", "C"]])

# ! me_frame.loc[row, col] me_frame.loc[]

# print(me_frame.loc[(me_frame["B"] < 0.3) & (me_frame["A"] > 0.4), ["B"]])

# print(me_frame.loc[(me_frame["B"] < 0.3) & (me_frame["A"] > 0.4)])

# print(me_frame.loc[[0, 1], :])

# ! df.T transposes our whole dataframe

# ? For getting value by integer index use iloc
# print(me_frame.iloc[150, 3])

me_frame.to_csv("Day6/PandasPrac/myData.csv", index=False)

# ! inplace=True will reflect our changes in original frame

me_frame.drop(["A", "D"], axis=1, inplace=True)

me_frame.loc[:, ["B"]] = "Hell or Heaven"

# print(me_frame.head())

me_frame.convert_dtypes()

print(me_frame.head())

print(type(me_frame["B"][0]))

df = pd.DataFrame(
    {
        "brand": ["Yum Yum", "Yum Yum", "Indomie", "Indomie", "Indomie"],
        "style": ["cup", "cup", "cup", "pack", "pack"],
        "rating": [4, 4, 3.5, 15, 5],
    }
)

df.drop_duplicates(subset="brand", inplace=True)

newdf = pd.DataFrame(
    {
        "name": ["Alfred", "Batman", "Catwoman"],
        "toy": [np.nan, np.nan, np.nan],
        "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
    }
)

newdf.dropna(inplace=True, how="all", axis=1)


print(newdf["name"].value_counts())
print(newdf["born"].value_counts(dropna=False))
