import pandas as pd

# HR DEPARTMENT                                                                                                
team = [
    ["Abdulmalek", "Software Engineer Manger", 21],
    ["Mohammed", "Bussines Manger", 20],
    ["Abody", "Developer", 18]
]

# ACOUNTING DEPARTMENT
age = [
    ["Abdulmalek", 5000],
    ["Abody", 4000],
    ["Mohammed", 4000]
]

df_team = pd.DataFrame(team, columns=["Name", "Job", "Age"])
df_age = pd.DataFrame(age, columns=["Name", "Income"])

print(df_team)
print("\n")
print(df_age)

new_df = pd.merge(df_team, df_age)

print("\n")
print(new_df)
