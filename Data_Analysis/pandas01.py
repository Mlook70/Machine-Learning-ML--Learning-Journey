import pandas as pd

#SERIES 

ls1 = ["Abdulmalek" , "Mohammed" , "Marwan" , "Layal" , "Renad"];

# ser = pd.Series(ls)

ser = pd.Series(ls1 , index=['A' , 'B' , 'C' , 'D' , 'E'])

print(ser)
print(ser.values)
print(ser.index)


print("\n")


ls2 = [10, 20, 30, 40, 50]

ser = pd.Series(ls2)

print(ser.describe())
#__________________________________________________________________________________________________________________________

# FRAME

ls1 = [10, 20, 30, 40, 50]
ls2 = [100, 200, 300, 400, 500]
ls3 = [1000, 2000, 3000, 4000, 5000]

frame = pd.DataFrame([ls1 , ls2 , ls3] , columns=['first' , 'second' , 'therd' , 'fourth' , 'fifth'])

print(frame)
print(frame.describe())
