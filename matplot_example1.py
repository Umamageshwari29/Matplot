import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({'A':[1,2,3,4,5], 'B':[2,4,6,8,10]})
df.plot(kind='line')
plt.show()
