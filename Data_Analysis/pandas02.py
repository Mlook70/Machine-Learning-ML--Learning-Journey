import pandas as pd 

# BANKING ACOUNTS

user1 = ["Abdulmalek" , 10000, 'A', 3000, "Abdulmalek@gmail.com", 9.5 ]
user2 = ["Abody", 5000, 'B', 2000, "Abody@gmail.com", 5]
user3 = ["Ahmed", 3000, 'C', 1500, "Ahmed@gmail.com", 3]
user4 = ["Mohammed", 9500, 'A', 2500, "Mohammed@gmail.com", 8.5]

df = pd.DataFrame([user1, user2, user3, user4] , 
                index=['A', 'B', 'C', 'D'],
                columns=["NAME" , "INCOME" , "CLASS" , "WITHDRAW" , "E-MAIL" , "SCORE"])
print(df)


print('\n')


new_df1 = df.drop(["SCORE" , "E-MAIL"] , axis = 1)
new_df2 = df.drop(["B", "C"], axis=0)
print(new_df1)
print(new_df2)


print('\n')


dt = df.dtypes
print(dt)


print('\n')


dt_select1 = df.select_dtypes(include=['int'])
dt_select2 = df.select_dtypes(exclude=['int'])
print(dt_select1)
print(dt_select2)
