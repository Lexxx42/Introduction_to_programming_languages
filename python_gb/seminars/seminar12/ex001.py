# -*- coding: utf-8 -*-
"""https://datalore.jetbrains.com/notebook/7XLGHiMrD4HKQPt8ekVv6S/ygNPpPj7hSr3UgNo8WGkTF/"""
# -- Sheet --

import pandas as pd

df = pd.read_csv("california_housing_train.csv")

df.head(10) # 10 starting

df.tail()

df.shape

df.isnull()

df.isnull().sum()

df.dtypes

df.columns

df['longitude']

df[['longitude','households']]

df[df['housing_median_age'] < 20]

df[(df['housing_median_age'] < 20) & (df['total_rooms'] > 20000)]

df.loc[df['housing_median_age'] < 20, 'total_rooms']

df.loc[df['housing_median_age'] < 20, ['total_rooms', 'total_bedrooms']]

df['population'].max()

df['population'].min()

df['population'].mean()

df['population'].sum()

df['population'].median()

df[['population', 'total_rooms']].median()

df.describe()

import seaborn as sns

sns.scatterplot(data=df, x='longitude', y='latitude')

sns.scatterplot(data=df, x='longitude', y='latitude', hue='total_rooms')

sns.scatterplot(data=df, x='longitude', y='latitude', hue='total_rooms', size='total_rooms', sizes=(100, 300))

cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
obj = sns.PairGrid(df[cols])
obj.map(sns.scatterplot)

sns.relplot(x='latitude', y='median_house_value', kind='line', data=df)

sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)

sns.histplot(data=df, x='median_income')

sns.histplot(data=df, x='housing_median_age')

sns.histplot(data=df[df['housing_median_age']>50], x='median_income')

df.loc[df['housing_median_age'] <= 20,'ade_group'] = 'Young'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50),'ade_group'] = 'Avr age'
df.loc[df['housing_median_age'] > 50,'ade_group'] = 'Old'
df

df.groupby('ade_group')['median_income'].mean().plot(kind='bar')

