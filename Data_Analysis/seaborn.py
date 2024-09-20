import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

area = [90 , 120 , 100]
price = [100000 , 130000 , 120000]
rooms = [2 , 2 , 3]

df = pd.DataFrame([area , price , rooms] , 
                columns=["Area" , "Price" , "Rooms"] , 
                index=["A","B","C"])
print(df)

print("\n")

c = df.corr()
print(c)

sns.heatmap(c)
plt.show()
