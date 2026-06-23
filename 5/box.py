import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

n = 100

data = pd.DataFrame()

for c in ['X', 'Y', 'Z']:
    data[c] = np.random.normal(size=n)

sns.boxplot(data=data)

plt.title("Box Plot")
plt.xlabel("Features")
plt.ylabel("Values")
plt.show()