import pandas as pd

# EMPLOYEES | الموظفين
users = [
    ["Abdulmalek", 21],
    ["Mohammed", 18],
    ["Abody", 20]
]

# DEPARTMENTS | الاقسام
jobs = [
    ["Developer"],
    ["Bussins Analysis"],
    ["UI/UX"]
]

df1 = pd.DataFrame(users, columns=["NAME", "AGE"])
df2 = pd.DataFrame(jobs, columns=["JOBS"])

print(df1)
print("\n")
print(df2)

print("\n")

concated = pd.concat([df1, df2], axis=1)

print(concated)

df1.insert(0, "LEVEL", 1)

print(df1)
