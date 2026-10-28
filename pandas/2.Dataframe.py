import pandas as pd 

# Dataframe = A tabular data structure with row and columns . (2 dimensional) || similar to excel sheets 

data ={
    "Name":["Spongebob","Patric","Squidward"],
    "Age":[25,30,40],
    "Salary":["$1000","$2000","$3000"]
}
df =pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3" ])
# #print(df)
# print(df.loc["Employee 1"])

# add a new column

df["Job"]=["Data Scientist","Web devloper","Cyber Security"]

#Add new row

new_row =pd.DataFrame([{"Name":"Sandy","Age":
35,"Salary":"$5000","Job":"Product Manager"}], index=["Employee 4"])

df=pd.concat([df,new_row])

print(df)