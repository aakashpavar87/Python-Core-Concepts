import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(3, 2), np.arange(3))

df.columns = ["A", "B"]

# print(df.describe())
# print(df.mean())
# print(df.corr())
# print(df.max())
# print(df.min())
# print(df.median())
# print(df.std())

new_df = pd.read_excel(io="Day6/PandasPrac/friends.xlsx", sheet_name="Sheet1", header=0)
print(new_df)
# ! Below line does nothing
# new_df.loc[3]["Name"] = "Hiren"
df_copy = new_df.copy()
# ! For modifying we should use below syntax .loc[row_name,col_name] = value
new_df.loc[3, "Name"] = "Hiren"

print(new_df.loc[3, "Name"])  # This works 🤣

print(df_copy)
print(new_df)

# with pd.ExcelWriter("Day6/PandasPrac/friends.xlsx") as writer:
#     df_copy.to_excel(writer, sheet_name="Sheet1", index=False)
#     new_df.to_excel(writer, sheet_name="Sheet2", index=False)
