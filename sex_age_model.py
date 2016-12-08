import pandas as pd
from sklearn.linear_model import LogisticRegression

def main():

	train = pd.read_csv("train.csv")
	test = pd.read_csv("test.csv")
	#print(df.to_string()) This just prints the spreadsheet. We don't need it.

	cat = ""
	col = ['Sex', 'Age']

	for word in col:
		cat = cat + word + "_"

	train['Sex'] = train['Sex'].map({"male": 0, "female": 1})
	test['Sex'] = test['Sex'].map({"male": 0, "female": 1})
	#Replaces the Sex strings of 'male' and 'female' with 0's and 1's respectively.

	age_med = row_median(train, test)
	#Finds the median age between both datasets. We aren't sure yet whether this is better or worse.

	train['Age'].fillna(age_med, inplace=True)
	test['Age'].fillna(age_med, inplace=True)
	#Adjusts NaN ages to the median



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


def row_median(train, test):
	a = train['Age'].sum() + test['Age'].sum()
	b = train.shape[0] + test.shape[0]
	return a//b

main()