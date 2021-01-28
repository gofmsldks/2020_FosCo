import pandas as pd
col = ['date','val1','val2']
data = pd.DataFrame([[1,2,3],[10,101,102],[20,201,22]],columns=col)
for i in data.index.values:
    print(i)