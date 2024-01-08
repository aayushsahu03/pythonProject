import pandas as pd
import numpy as np


def func():

    df = pd.DataFrame([[1,2,3],[4,5,6]])
    df2 = df
    #print(df)
    df2['diff'] = df2[1]-df2[0]
    
    df3 = df
    df3_roll = df3[df3[2]>4]

    del df,df3
    return df2, df3_roll
df1,df2 = func()

print(df1,'*'*10,sep='\n')
print(df2)


a = np.arange(10)
cond_list = [a<4]
choice_list = [a]
print(np.select(cond_list, choice_list))
df1.plot(kind='hist').show()