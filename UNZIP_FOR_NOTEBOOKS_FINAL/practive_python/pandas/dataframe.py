from pydoc import describe
from this import d
import pandas as pd

df = pd.read_csv("C:\\Users\\PV\\Desktop\\UNZIP_FOR_NOTEBOOKS_FINAL\\DATA\\tips.csv")

#obtaining basic information about dataframe
columns = df.columns
index = df.index
head = df.head()
head_10 = df.head(10)
tail = df.tail()
tail_10 = df.tail(10)
info = df.info()
len = len(df)
describeOfdf = df.describe()


# selecing and indexing
total_bill = df['total_bill']
bill_tip = df[['total_bill','tip']]

# create a new columns
df['new_percen_tip'] = 100*df['tip']/df['total_bill']

#ajusting existing columns
df = df.drop('new_percen_tip',axis=1)
df = df.set_index('Payment ID')
df = df.reset_index()

#rows
singleRow = df.iloc[0]

