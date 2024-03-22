import pandas as pd
items={}
Data1=dict()
Data2=dict()
for i in range(2):
    name1=input("coloumn name :")
    for i in range(int(input("number of elements:"))):
        print('Enter the item name:',end=' ')
        name=input()
        if name1 not in Data1:
            Data1[name1]=[]
            Data1[name1].append(name)
        else:
            Data1[name1].append(name)
for i in range(2):
    name1=input("coloumn name :")
    for i in range(int(input("number of elements:"))):
        print('Enter the item name:',end=' ')
        name=input()
        if name1 not in Data2:
            Data2[name1]=[]
            Data2[name1].append(name)
        else:
            Data2[name1].append(name)
# print("ITEM :",Data1)
# print("ITEM :",Data2)

df1=pd.DataFrame(Data1)
df2=pd.DataFrame(Data2)

print("list of dataframe1")
print(pd.DataFrame.from_dict(Data1))
print("list of dataframe2")
print(pd.DataFrame.from_dict(Data2))

print("list of dataframe after merging two dataframes")
df3=pd.merge(df1,df2,on='name')
print(df3)

print("details of student who belongs to section :")
df4=df3[df3['sec']==input()]
print(df4)

print("details of student after sorting them in decending order")
df5=df4.sort_values(by='att',ascending=False)
print(df5)

print("details of student after sorting them in ascending order")
df6=df4.sort_values(by='att',ascending=True)
print(df6)

print("details of student who is less regular to classes")
print(df4.min())

print("details of student who is more regular to classes")
print(df4.max())