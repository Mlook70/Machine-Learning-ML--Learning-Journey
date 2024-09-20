import matplotlib.pyplot as plt 
import numpy as np 

# THE PRICES AND AREAS FOR 2 TOWERS

plt.style.use("dark_background")
# plt.style.use("seaborn")

area = np.array([100 , 200 , 300 , 400 , 500])
price1 = np.array([1000, 2000, 3000, 4000, 5000])
price2 = np.array([1500, 2500, 3500, 4000, 5000])

plt.plot(area , price1, 'b' , label = "Tower 1")
plt.plot(area, price2, 'r', label="Tower 2")
plt.legend()

plt.title('LINEAR REGERASSION')
plt.xlabel("Area")
plt.ylabel("Price")

plt.legend()

plt.show()

#_________________________________________________________________________

# plt.style.use("dark_background")
# area = np.array([100 , 200 , 300 , 400 , 500])
# price1 = np.array([1000, 2000, 3000, 4000, 5000])
# price2 = np.array([1500, 2500, 3500, 4000, 5000])



# plt.subplot(2, 1, 1)
# plt.plot(area , price1 , 'b' , label = "Tower1")
# plt.legend()
# plt.title('LINEAR REGERASSION')
# plt.xlabel("Area")
# plt.ylabel("Price")


# plt.subplot(2, 1, 2)
# plt.plot(area, price2, 'r', label="Tower2")
# plt.legend()
# plt.xlabel("Area")
# plt.ylabel("Price")

# # a = plt.axes()
# # a.set(title="LINEAR REGRASSION" , xlabel="Area" , ylabel="Price")

# plt.show()
