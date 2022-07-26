import pandas as pd
df = pd.read_csv('fingerprint.csv')
df1= df.set_index('Title')
#df1 = df1.iloc[:, 0:10082]
cout = 0
list1 = []
for j in range(len(df1.columns)):
    if ((df1.iloc[:,j][0] == 1) or (df1.iloc[:,j][1] == 1) or (df1.iloc[:,j][2] == 1) or (df1.iloc[:,j][3] == 1)or (df1.iloc[:,j][4] == 1)or (df1.iloc[:,j][5] == 1)or (df1.iloc[:,j][6] == 1)or (df1.iloc[:,j][7] == 1)):
        list1.append(df1.columns[j])
        cout += 1
#print(cout)
#print(list1)

df2 = df1[list1].copy()
df2.to_csv("output_fingerprint.csv")
hydrophobic = []
acceptor = []
for i in list1:
    v1 = (i.split("_"))
    if v1[1] == "hydrophobic":
        hydrophobic.append(i)
    elif v1[1] == "acceptor":
        acceptor.append(i)
       
print(acceptor)
df3 = df2[acceptor].copy()
df3.to_csv("out_acceptor.csv")

#print(backbone)
