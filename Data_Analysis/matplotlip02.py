import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Today's sales FOR A SHOPE

plt.style.use('dark_background')

sels_per_day = [['mon', 10],['tus',20] ,['wen',30] ,['the',50] ,['fri',40] ,['sut',20] ,['sun' , 40]]
frame = pd.DataFrame(sels_per_day , columns=["DAY" , "SELES"])
print(frame)

days = ['mon', 'tus', 'wen','the', 'fri', 'sut', 'sun']
seles = [10, 20, 30, 50, 40, 20, 40]

plt.title("SELES PER DAY")
plt.xlabel("DAY")
plt.ylabel("SELES")

plt.scatter(days, seles, color='b', marker='x', s=100)
plt.plot(days, seles, color='r')
plt.bar(days, seles, edgecolor='black', facecolor='white')

plt.show()