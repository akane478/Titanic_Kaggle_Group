import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

def main():

	train = pd.read_csv("train.csv")
	test = pd.read_csv("test.csv")
	#print(df.to_string()) This just prints the spreadsheet. We don't need it.

	del train['Name']
	del train['SibSp']
	del train['Parch']
	del train['Ticket']
	del train['Cabin']
	del train['Embarked']

	train.dropna(inplace=True)

	train['Sex'] = train['Sex'].map({"male": 0, "female": 1})
	test['Sex'] = test['Sex'].map({"male": 0, "female": 1})
	#Replaces the Sex strings of 'male' and 'female' with 0's and 1's respectively.

	age_med = col_median(train, test, 'Age')
	fare_med = col_median(train, test, 'Fare')
	#Finds the median age and fare between both datasets. We aren't sure yet whether this is better or worse.
	
	test['Age'].fillna(age_med, inplace=True)
	test['Fare'].fillna(fare_med, inplace=True)
	#Adjusts NaN ages  and fare to the median

	test['Pclass'].fillna(3, inplace=True)

	train['YMCA'] = np.where(((train['Age']<=16) & (train['Sex']==0)) | train['Sex']==1 , 1, 0)
	test['YMCA'] = np.where(((test['Age']<=16) & (test['Sex']==0)) | test['Sex']==1 , 1, 0)

	cat = ""
	col = ['YMCA', 'Sex', 'Pclass', 'Fare']

	for word in col:
		cat = cat + word + "_"

	lr = LogisticRegression()
	#Setting up logistical regression, which allows the computer to make predictions
	lr.fit(train[col],train['Survived'])
	#Making a fit with just sex and age

	print(lr.score(train[col],train['Survived']))
	#Testing it on itself

	test['Survived'] = lr.predict(test[col])
	#Makes predictions on the test file

	output = ['PassengerId', 'Survived']
	#Prints the results to a submission
	test[output].to_csv(cat+'submission.csv', index=False)


def col_median(train, test, string):
	a = train[string].sum() + test[string].sum()
	b = train.shape[0] + test.shape[0]
	return a/b

main()
#Results in 77.033% accuracy