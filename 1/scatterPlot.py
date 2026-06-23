from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["Species"] = iris.target

sns.scatterplot(data=df,
                x="sepal length (cm)",
                y="sepal width (cm)",
                hue="Species")

plt.title("Iris Scatter Plot")
plt.show()