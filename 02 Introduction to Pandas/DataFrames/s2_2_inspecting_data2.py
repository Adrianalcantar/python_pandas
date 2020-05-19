import pandas as pd
df = pd.read_csv('../../sample_data/02 Introduction to pandas/intel.csv')


### print df to make sure it works
### print(df)


### how to check data type
### print(type(df))


### How to check dataframe shape
### print(df.shape)


### How to view colum names
### print(df.columns)


### inspect first rows of data
### print(df.head(10))


### Inspect last roes of data
### print(df.tail(2))


### view summary of dataframe(df) info
### print(df.info())

### view open colum
###open = df['Open']
### print(open)


###print(open.head()) to view the first rows

### view one or more colums side by side
### print(df[['Open', 'Close']].head())


### Using the describe method
### print(df.describe())
