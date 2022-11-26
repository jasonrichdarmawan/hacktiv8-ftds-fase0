import joblib
import pandas as pd
import numpy as np

with open('./pipe.pkl', 'rb') as file_2:
    pipe = joblib.load(filename=file_2)

df = pd.DataFrame(
    data={
        'PAYMENTS': [np.nan, 100, np.nan],
        'MINIMUM_PAYMENTS': [100, 100, 100]
    }
)

print(pipe.transform(X=df))