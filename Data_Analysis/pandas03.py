import pandas as pd

# BANKING ACOUNTS WITH LOSS INFO

user1 = ["Abdulmalek", 10000, 'A', None, "Abdulmalek@gmail.com", 9.5]
user2 = ["Abody", 5000, 'B', 2000, "Abody@gmail.com", 5]
user3 = ["Ahmed", 3000, 'C', 1500, None, 3]
user4 = ["Mohammed", 9500, 'A', 2500, "Mohammed@gmail.com", 8.5]

df = pd.DataFrame([user1, user2, user3, user4],
                index=['A', 'B', 'C', 'D'],
                columns=["NAME", "INCOME", "CLASS", "WITHDRAW", "E-MAIL", "SCORE"])
print(df)

print('\n')

new_data = df.dropna() # Remove all the rows with None value
print(new_data)

print('\n')

# replace all the data in None value with the value you put
df["E-MAIL"].fillna("UNKNOWN", inplace=True)
print(df)


