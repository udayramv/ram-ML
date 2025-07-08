import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression
from sklearn import metrics as mtrcs
import numpy as numpy
import pandas as pandas
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler

dataframe=pandas.read_csv('monet.csv')
print(dataframe)
dataframe.shape
dataframe.describe()
dataframe.columns
dataframe['Size']=dataframe['WIDTH']*dataframe['HEIGHT']
print(dataframe)

pyplot.scatter(dataframe['Size'],dataframe['PRICE'])
pyplot.xlabel("Size")
pyplot.ylabel("Price")
pyplot.title("Size and Price Comparison")
x, y = numpy.polyfit(dataframe['Size'], dataframe['PRICE'], 1)
pyplot.plot(dataframe['Size'], x*dataframe['Size']+y, color='green')

magnitude = dataframe.iloc[:, -1].values
RateParameter = dataframe.iloc[:, 0].values


Horizontal_check, Horizontal_check1, vertical_check, vertical_check1 = tts(magnitude, RateParameter, test_size = 0.2, random_state = 0)

Horizontal_check= Horizontal_check.reshape(-1, 1)
Horizontal_check1= Horizontal_check1.reshape(-1, 1)
vertical_check= vertical_check.reshape(-1, 1)
vertical_check1= vertical_check1.reshape(-1, 1)

LR_algo = LinearRegression()
LR_algo.fit(Horizontal_check,vertical_check)

vertical_pred = LR_algo.predict(Horizontal_check1)

print('Error of Mean Square:', mtrcs.mean_squared_error(vertical_check1,vertical_pred))
print('Error of Root Mean Square:', numpy.sqrt(mtrcs.mean_squared_error(vertical_check1,vertical_pred)))

pyplot.scatter(dataframe['WIDTH'],dataframe['PRICE'])
pyplot.xlabel("Width")
pyplot.ylabel("Price")
pyplot.title("Width and Price Comparison")
x, y = numpy.polyfit(dataframe['WIDTH'], dataframe['PRICE'], 1)
pyplot.plot(dataframe['WIDTH'], x*dataframe['WIDTH']+y, color='green')

ParameterWidth = dataframe.iloc[:, 2].values
RateParameter = dataframe.iloc[:, 0].values

Horizontal_check, Horizontal_check1, vertical_check, vertical_check1 = tts(ParameterWidth, RateParameter, test_size = 0.2, random_state = 0)

Horizontal_check= Horizontal_check.reshape(-1, 1)
Horizontal_check1= Horizontal_check1.reshape(-1, 1)
vertical_check= vertical_check.reshape(-1, 1)
vertical_check1= vertical_check1.reshape(-1, 1)

LR_algo = LinearRegression()
LR_algo.fit(Horizontal_check,vertical_check)

vertical_pred = LR_algo.predict(Horizontal_check1)

print('Error of Mean Square:', mtrcs.mean_squared_error(vertical_check1,vertical_pred))
print('Error of Root Mean Square:', numpy.sqrt(mtrcs.mean_squared_error(vertical_check1,vertical_pred)))

# Task 2
X = dataframe.iloc[:, 1:].values
y = dataframe.iloc[:, 0].values

Horizontal_check, Horizontal_check1, vertical_check, vertical_check1 = tts(X, y, test_size = 0.2, random_state = 0)

StandardScaler_algo = StandardScaler()
Horizontal_check = StandardScaler_algo.fit_transform(Horizontal_check)
Horizontal_check1 = StandardScaler_algo.transform(Horizontal_check1)

LR_algo = LinearRegression()
LR_algo.fit(Horizontal_check,vertical_check)

vertical_pred = LR_algo.predict(Horizontal_check1)
print('Error of Mean Square:', mtrcs.mean_squared_error(vertical_check1,vertical_pred))
print('Error of Root Mean Square:', numpy.sqrt(mtrcs.mean_squared_error(vertical_check1,vertical_pred)))