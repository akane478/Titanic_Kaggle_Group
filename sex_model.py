import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
#print(df.to_string()) This just prints the spreadsheet. We don't need it.

cat = "sex"
col = ['Sex']

train['Sex'] = train['Sex'].map({"male": 0, "female": 1})
test['Sex'] = test['Sex'].map({"male": 0, "female": 1})
#Replaces the Sex strings of 'male' and 'female' with 0's and 1's respectively.

lr_gender = LogisticRegression()
#Setting up logistical regression, which allows the computer to make predictions
lr_gender.fit(train[col],train['Survived'])
#Making a fit with just sex

print(lr_gender.score(train[col],train['Survived']))
#Testing it on itself

test['Survived'] = lr_gender.predict(test[col])
#Makes predictions on the test file

output = ['PassengerId', 'Survived']
#Prints the results to a submission
test[output].to_csv(cat+'_submission.csv', index=False)