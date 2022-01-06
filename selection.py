# Selected by column names
Df1=Df.loc[:,['Column A','Column B']]
           
# Selected by index      
Df1=Df.iloc[:,3]

# Selected by index and adding range on raws
Df1=DF.iloc[1:3,:]

# Selected by column condition
Df.loc[:,[zh_name]=='XXX']

# Selected by column condition
Df[Df.zh_name=='XXX']