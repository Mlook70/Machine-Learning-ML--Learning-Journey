import pandas as pd 

# الموظفين
employees = [
    ["Ali" , "Engineering"],
    ["Abody" , "Bussines"],
    ["Khaled", "Bussines"],
    ["Ahmed", "Engineering"]
]

# مدراء الموظفين
mangers = [
    ["Abdulmalek", "Engineering"],
    ["Mohammed", "Bussines"],
]

df_employees = pd.DataFrame(employees , columns=["Employees" , "Department"])
df_mangers = pd.DataFrame(mangers, columns=["Mangers", "Department"])

print(df_employees)
print("\n")
print(df_mangers)

new_df = pd.merge(df_employees, df_mangers)

print("\n")
print(new_df)
