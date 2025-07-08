import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('winequality-red.csv')
df.shape

df.columns
df.head()

df.describe()
df.dtypes

df.isnull().sum()
df['quality'].value_counts()
df.corr()['quality'].sort_values(ascending=False)
df['quality'] = df['quality'].apply(lambda x: 1 if x >= 7 else 0)
df['quality'].value_counts()
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
df.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logistic_reg.score(X_test, y_test)))

y_pred=np.where(y_pred>=7, 1, 0)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
