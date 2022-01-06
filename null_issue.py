# Finding Null data from certain column within a DataFrame 
Df1=Df['ColumnA'].isnull()  # Adding a boolean mask
Df2=Df[Df1]

#Finding 