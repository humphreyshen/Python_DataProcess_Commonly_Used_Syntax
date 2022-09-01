# Create DataFrame
df=pd.Dataframe(data=None, index=None, columns=None, dtype=None, copy=None)

# Drop Column
df1=df.drop(['A', 'B'], axis=1)

# Insert Column
df1=df.insert(loc,
              column,
              value,
              allow_duplicates=False)

