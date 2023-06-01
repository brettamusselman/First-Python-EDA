#Project: rainInAustraliaEDA
#Purpose: Replicate EDA from previously found study
#Author: Brett Musselman
#Date: 28 May

#Import various libraries(some may be useless but I just wanted to download all of the important ones)
#from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
#import os
import pandas as pd
import seaborn as sns

#Create data frame from reading CSV
nRowsRead = None
df1 = pd.read_csv(r'C:\Users\brett\Downloads\archive\weatherAUS.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'weatherAUS.csv'

#Graph scatterplot matrix
df2 = df1.select_dtypes(include=[np.number])
df2 = df2[[col for col in df2 if df2[col].nunique() > 1]]
df3 = df2[['MinTemp','MaxTemp','Rainfall','Evaporation','WindGustSpeed','Sunshine']]
scatterMatrixAus = plt.title('Scatterplot Matrix')
scatterMatrix = pd.plotting.scatter_matrix(df3, diagonal='hist')
for ax in scatterMatrix.flatten():
    ax.xaxis.label.set_rotation(15)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')
plt.show()


#Graph correlation matrix
#corrMatrixAus = plt.figure('Heatmap')
#correlationMatrix = sns.heatmap(df2.corr(), cmap=sns.diverging_palette(20, 220, n=200), square=True)
#correlationMatrix.set_xticklabels(correlationMatrix.get_xticklabels(), rotation=45, horizontalalignment='right')
#plt.title('Heatmap')
#plt.show()

#Open a text file and write a description of each column
#with open('describe_AUS_data.txt', 'a') as describeFile:
    #describeFile.truncate(0)
    #columnsList = list(df1.columns)
    #for column in columnsList:
        #describeColumn = df1[column].describe()
        #stringColumn = str(describeColumn)
        #describeFile.write(stringColumn)


#Drop duplicate values (there are none)
#print(df1.duplicated().sum())

#Replace null values with median (numerical) and mode (categorical)
#Numerical variables: MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am,
#Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm
#Categorical variables: WindGustDir, WindDir9am, WindDir3pm, RainToday, RainTomorrow
medianMinTemp = df1['MinTemp'].median()
medianMaxTemp = df1['MaxTemp'].median()
medianRainfall = df1['Rainfall'].median()
medianEvaporation = df1['Evaporation'].median()
medianSunshine = df1['Sunshine'].median()
medianWindGustSpeed = df1['WindGustSpeed'].median()
medianWindSpeed9am = df1['WindSpeed9am'].median()
medianWindSpeed3pm = df1['WindSpeed3pm'].median()
medianHumidity9am = df1['Humidity9am'].median()
medianHumidity3pm = df1['Humidity3pm'].median()
medianPressure9am = df1['Pressure9am'].median()
medianPressure3pm = df1['Pressure3pm'].median()
medianCloud9am = df1['Cloud9am'].median()
medianCloud3pm = df1['Cloud3pm'].median()
medianTemp9am = df1['Temp9am'].median()
medianTemp3pm = df1['Temp3pm'].median()

modeWindGustDir = df1['WindGustDir'].mode().values[0]
modeWindDir9am = df1['WindDir9am'].mode().values[0]
modeWindDir3pm = df1['WindDir3pm'].mode().values[0]
modeRainToday = df1['RainToday'].mode().values[0]
modeRainTomorrow = df1['RainTomorrow'].mode().values[0]

df1['MinTemp'] = df1['MinTemp'].replace(np.nan,medianMinTemp)
df1['MaxTemp'] = df1['MaxTemp'].replace(np.nan,medianMaxTemp)
df1['Rainfall'] = df1['Rainfall'].replace(np.nan,medianRainfall)
df1['Evaporation'] = df1['Evaporation'].replace(np.nan,medianEvaporation)
df1['Sunshine'] = df1['Sunshine'].replace(np.nan,medianSunshine)
df1['WindGustSpeed'] = df1['WindGustSpeed'].replace(np.nan,medianWindGustSpeed)
df1['WindSpeed9am'] = df1['WindSpeed9am'].replace(np.nan,medianWindSpeed9am)
df1['WindSpeed3pm'] = df1['WindSpeed3pm'].replace(np.nan,medianWindSpeed3pm)
df1['Humidity9am'] = df1['Humidity9am'].replace(np.nan,medianHumidity9am)
df1['Humidity3pm'] = df1['Humidity3pm'].replace(np.nan,medianHumidity3pm)
df1['Pressure9am'] = df1['Pressure9am'].replace(np.nan,medianPressure9am)
df1['Pressure3pm'] = df1['Pressure3pm'].replace(np.nan,medianPressure3pm)
df1['Cloud9am'] = df1['Cloud9am'].replace(np.nan,medianCloud9am)
df1['Cloud3pm'] = df1['Cloud3pm'].replace(np.nan,medianCloud3pm)
df1['Temp9am'] = df1['Temp9am'].replace(np.nan,medianTemp9am)
df1['Temp3pm'] = df1['Temp3pm'].replace(np.nan,medianTemp3pm)

df1['WindGustDir'] = df1['WindGustDir'].replace(np.nan,modeWindGustDir)
df1['WindDir9am'] = df1['WindDir9am'].replace(np.nan,modeWindDir9am)
df1['WindDir3pm'] = df1['WindDir3pm'].replace(np.nan,modeWindDir3pm)
df1['RainToday'] = df1['RainToday'].replace(np.nan,modeRainToday)
df1['RainTomorrow'] = df1['RainTomorrow'].replace(np.nan,modeRainTomorrow)

#print(df1.isnull().sum())



#Scatterplots with colored dots for yes or no with rain tomorrow
#fig, ax = plt.subplots()
#colors= {'No':'Blue', 'Yes':'Green'}
#humVsTemp = ax.scatter(df1['Humidity3pm'], df1['Temp3pm'], c=df1['RainTomorrow'].map(colors))
#ax.set_xlabel('Humidity3pm')
#ax.set_ylabel('Temp3pm')
#ax.legend(colors)
#plt.show()


#colors= {'No':'Blue', 'Yes':'Green'}
#fig, ax = plt.subplots()
#pressVsHum = ax.scatter(df1['Humidity3pm'], df1['Pressure9am'], c=df1['RainTomorrow'].map(colors))
#ax.set_xlabel('Humidity3pm')
#ax.set_ylabel('Pressure9am')
#ax.legend(colors.keys())
#plt.show()


#fig, ax = plt.subplots()
#colors= {'No':'Blue', 'Yes':'Green'}
#minVsMax = ax.scatter(df1['MaxTemp'], df1['MinTemp'], c=df1['RainTomorrow'].map(colors))
#ax.set_xlabel('MaxTemp')
#ax.set_ylabel('MinTemp')
#ax.legend(colors)

#Boxplots of significant features with yes or no separate graphs
#sns.boxplot(x=df1['RainTomorrow'], y=df1['Cloud9am'])

#sns.boxplot(x=df1['RainTomorrow'], y=df1['Sunshine'])

#sns.boxplot(x=df1['RainTomorrow'], y=df1['Humidity3pm'])
#plt.show()