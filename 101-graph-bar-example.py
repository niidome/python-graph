import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_excel("data/population.xlsx", index_col=0)
# print(df)

df["総人口"].plot.bar()
plt.show()
