import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(100,4),
    columns= ['a','b','c','d'])
print(data)