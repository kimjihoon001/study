# pandas_module.py

import pandas as pd
# print(pd.__version__)

data = [10, 20, 30]
series = pd.Series(data)
print(series)

print('-------------')

data = {'a':10, 'b':20, 'c':30}
series=pd.Series(data)
print(series)

