import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

n = 100

data = pd.DataFrame()

for c in ['X', 'Y']:
    data[c] = np.random.normal(size=n)

data['Category'] = np.random.choice(['A', 'B', 'C'], n)

sns.scatterplot(data=data, x='X', y='Y', hue='Category')

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()