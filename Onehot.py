import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data_one_hot = pd.get_dummies(data, columns=['whoAmI'])
data_one_hot.head()