import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/temperature.csv", index_col=0, encoding="shift_jis")
# print(df)

df["最高気温"].plot(color="red")
df["最低気温"].plot(color="blue")

plt.legend(loc="lower right")
plt.show()
