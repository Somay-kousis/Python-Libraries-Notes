import pandas as pd
import numpy as np

series = pd.Series([1,2,3,np.nan,6,8])

dates = pd.date_range("20130101", periods=6)
df     = pd.DataFrame(np.random.randn(6,4), index=dates, columns=("A","B","C","D"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

df2.dtypes
df2.to_numpy()
df.head() # check first 5 rows
df.tail(3) # check last 3 rows
df.describe() #Gives important details like mean of data 
df.T # tranposes the data
df.sort_index(axis=1, ascending=False) # axis = 1, rows       0 = columns
df.sort_values(by="B") #aranged on thebasis of B

# DataFrame.at(), DataFrame.iat(), DataFrame.loc() and DataFrame.iloc().
# at() single cell, loc() multiple cell BY LABEL
# iat() single cell, iloc() multiple cell BY INDEX

df = pd.DataFrame({"A": [10, 20], "B": [30, 40]}, index=["x", "y"])
# note:- column A ka data, B ka data, index
print(df.at["x", "A"]) 

df["A"] #To check data of A column
df["20130102":"20130104"] # include 04 too

df.loc["20130102":"20130104", ["A", "B"]] # using name of rows and columns
df.iloc[3:5, 0:2]                         # using index

df[df["A"] > 0] # row wise sfilter
df[df > 0]      # element wise filter

df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"] # adding a column is so easy 

df2[df2["E"].isin(["two", "four"])] #using isin

df.mean(axis=1) #rows ka mean
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2) #shift pubshed data towards bottom by 2 so 1,2 got naN because of that

# Missing data
#
#

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1

#                    A         B         C    D    F    E
# 2013-01-01  0.000000  0.000000 -1.509059  5.0  NaN  1.0
# 2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0  NaN
# 2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0  NaN

df1.dropna(how="any") #Drops any rows that have missing data:
df1.fillna(value=5)
pd.isna(df1) #nan = true 

df.agg(lambda x: np.mean(x) * 5.6) # is applied column wise and changes shape of data set
df.transform(lambda x: x * 101.2) #applies on each element

s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts() #tells numbers of occurances

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower() #using str you can command all strings in a data set

df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]] # break it into pieces
pd.concat(pieces)

left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
pd.merge(left, right, on="key") #on attribute is most interesting

# By “group by” we are referring to a process involving one or more of the following steps:

# Splitting the data into groups based on some criteria
# Applying a function to each group independently
# Combining the results into a data structure


df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
#      A      B         C         D
# 0  foo    one  1.346061 -1.577585
# 1  bar    one  1.511763  0.396823
# 2  foo    two  1.627081 -0.105381
# 3  bar  three -0.990582 -0.532532
# 4  foo    two -0.441652  1.453749
# 5  bar    two  1.211526  1.208843
# 6  foo    one  0.268520 -0.080952
# 7  foo  three  0.024580 -0.264610
df.groupby("A")[["C", "D"]].sum()
# A           C         D                     
# bar  1.732707  1.073134
# foo  2.824590 -0.574779
df.groupby(["A", "B"]).sum()



#Reshaping

arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
 ]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2
#                      A         B
# first second                    
# bar   one    -0.727965 -0.589346
#       two     0.339969 -0.693205
# baz   one    -0.339355  0.593616
#       two     0.884345  1.591431

stacked = df2.stack(future_stack=True) #columns are movedor you can say merged 
# first  second   
# bar    one     A   -0.727965
#                B   -0.589346
#        two     A    0.339969
#                B   -0.693205
# baz    one     A   -0.339355
#                B    0.593616
#        two     A    0.884345
#                B    1.591431



stacked.unstack(0) #unstack bar baz as 0 index level
stacked.unstack(1) #unstack one two as 0 index level
stacked.unstack(2)=stacked.unstack() #unstack A and B as 0 index level


#After stack we have pivot
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]) #it sets up data exactly like this

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
ts
# 2012-03-06    1.857704
# 2012-03-07   -1.193545
# 2012-03-08    0.677510
# 2012-03-09   -0.153931
# 2012-03-10    0.520091

rng = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample("5Min").sum()
#resample makes pack of 5 minutes, initally we had 100s 1:40 so we will have only 1 cell.

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)

ts.tz_localize("UTC") #it was always this but was never said 
# tz_convert("US/Eastern")


#Categoricals
#
#
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)

df["grade"] = df["raw_grade"].astype("category") #isnt saved as raw string but made a category, good practice

new_categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.rename_categories(new_categories) # a b e are vg and vb now

df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
# we have made more categories even if they are not in use

df.sort_values(by="grade") #while definign category, the one at first comes at first
df.groupby("grade", observed=False).size() #tells number of occurances of each category, including one with 0

# import export
df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
df.to_csv("foo.csv")
pd.read_csv("foo.csv")

df.to_parquet("foo.parquet")
pd.read_parquet("foo.parquet")

df.to_excel("foo.xlsx", sheet_name="Sheet1")
pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])

# na_values=["NA"]
# This tells Pandas:
# ➡️ "If you see the text "NA" in the Excel file, treat it as a missing value (NaN)"

# This controls which column to use as the index of the DataFrame when reading the Excel file.
# index_col=None:
# → "Don't treat any column as the index. Just use the default 0, 1, 2…"
