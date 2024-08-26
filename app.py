import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

means = df['salary'].mean()

print(f'Средняя зарплата сотрудников: {means}')

df = df.query('age > 30')

print(f'Сотрудники старше 30 лет:')
print(df)