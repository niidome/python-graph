import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_excel("data/child.xlsx", index_col=0)
# print(df)

color_list = ["blue", "green", "yellow", "orange", "red"]
df["％"].plot.pie(colors=color_list)

plt.title("子供の人数")
plt.show()
