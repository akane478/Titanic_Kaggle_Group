data = pd.read_csv('../input/train.csv')
data.head() // displays the data
data.describe() //quickly analyzes the data
data['Age'].fillna(data['Age'].median(), inplace=True) // fills in the non-existent age data with averages

survived_sex = data[data['Survived']==1]['Sex'].value_counts()
dead_sex = data[data['Survived']==0]['Sex'].value_counts()
df = pd.DataFrame([survived_sex,dead_sex])
df.index = ['Survived','Dead']
df.plot(kind='bar',stacked=True, figsize=(15,8))

// displays a graph of survival based on gender

figure = plt.figure(figsize=(15,8))
plt.hist([data[data['Survived']==1]['Age'],data[data['Survived']==0]['Age']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Survived','Dead'])
plt.xlabel('Age')
plt.ylabel('Number of passengers')
plt.legend()

// displays a graph of survival based on age
