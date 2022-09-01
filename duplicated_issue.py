# Droppping duplicated data from certain column within a DataFrame
Df1=Df.drop_duplicates(subset=['Coumn A'], Keep=False) # drop all of the duplicated data

# Finding duplicated data from certain column within a DataFrame
Df1=Df.duplicated(subset=['Column A'], Keep=False) # Keep all of the duplicated data
Df1=Df.duplicated(subset=['Column A'], Keep='first') # Keep the first data of the duplicated data set
Df1=Df.duplicated(subset=['Column A'], Keep='last') # Keep the last data of the duplicated data set