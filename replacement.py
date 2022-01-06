# \r replacement
df.replace({'\r':''},regex=True)

# \n replacement
df.replace({'\n':''},regex=True)

# \u3000 replacement
df.replace(u'\u3000',u'',regex=True)

# 'space' replacement
df.replace(' ','',regex=True)