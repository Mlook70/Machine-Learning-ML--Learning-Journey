import pandas as pd 

# STATISTICS FOR DEPARTMENTS

data =[
    ["Engineer" , 2500],
    ["Accountant", 2000],
    ["Designer", 2000],
    ["Engineer", 3000],
    ["Accountant", 2500],
    ["Designer", 2500],
]

df = pd.DataFrame(data, columns=["Job", "Income"])

job_count = df.groupby("Job").count()
job_mean = df.groupby("Job").mean()

print(job_count)
print(job_mean)
