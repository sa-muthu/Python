import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("03.01 - Pokemon copy.csv")

type_count = df["Type1"].value_counts(ascending = True)

plt.barh(type_count.index, type_count.values, color = "black", edgecolor = "lime")

plt.title("spooder maan")

plt.xlabel("aaaa")
plt.ylabel("eee")

plt.tight_layout()
plt.show()