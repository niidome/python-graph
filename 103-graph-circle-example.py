import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_excel("data/child.xlsx", index_col=0)
# print(df)

df["％"].plot.pie()
plt.show()
