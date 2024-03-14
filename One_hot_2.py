import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

uniquelabels = data['whoAmI'].unique()
onehotdata = pd.DataFrame(0, columns=uniquelabels, index=range(len(data)))

for i, label in enumerate(data['whoAmI']):
    onehotdata.loc[i, label] = 1

onehotdata.head()