import pandas as pd
from datasets import load_dataset


dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])
# X = df.drop(columns=['default.payment.next.month'])
# y = df['default.payment.next.month'].values

# remove duplicates and don't create copy of df     //////
df.drop_duplicates(inplace = True)

# calculating correlation       //////
dfLimit = pd.DataFrame(dataset['train']["limit_bal"])
dfAge = pd.DataFrame(dataset['train']["age"])

cor = dfLimit.corrwith(dfAge)
# print(cor)

# calculating sum of the transactions   /////

# # print(df.loc[::,['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']])
df['bill_amt_X'] = df.iloc[:, 8:14].sum(axis = 1)
# print(df[:3])

# finding 10 the oldest clients     /////
tenOldest = df.nlargest(10, 'age')

edDict = {1: "Graduate School", 2: "University", 3: "High school", 4: "Primary School", 5: "Other", 6: "Unknown"}
edColumns = ["education0", "education1", "education2", "education3", "education4", "education5", "education6"]
columns = []

for i in range(0, 10):
    for j in range(22, 29):
        if tenOldest.iloc[i, j] == 1.0:
            columns.append(j - 22)

print(columns)
edNames = pd.DataFrame({'education': [edDict[key] for key in columns]}, index = tenOldest.index)

dfOldest = pd.DataFrame()
dfOldest['limit_bal'] = tenOldest['limit_bal']
dfOldest['age'] = tenOldest['age']
dfOldest['education'] = edNames
dfOldest['bill_amt_X'] = tenOldest['bill_amt_X']

print(dfOldest)


# matplotlib    /////
