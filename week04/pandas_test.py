import pandas as pd
import numpy as np

# 预备数据
data_age = pd.DataFrame({
    "id": np.random.randint(1,1500, 300),
    "age": np.random.randint(15, 50, 300),
    "gender": np.random.randint(0, 2, 300)
})

data_salary = pd.DataFrame({
    "id": np.random.randint(10,1500, 300),
    "salary": np.random.randint(800, 20000, 300)
})

print(data_age.head())
print("-"*50)
print(data_salary.head())

# 1. SELECT * FROM data
print(data_salary)

print("-"*50)

# 2. SELECT * FROM data LIMIT 10
print(data_salary.head(10))

print("-"*50)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data_salary['id'])

print("-"*50)

# 4. SELECT COUNT(id) FROM data
print(data_salary['id'].count())

print("-"*50)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data_age[(data_age['id'] < 1000) & (data_age['age']> 30)])

print("-"*50)

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(data_age.groupby('gender').agg({"id": 'count'}))

print("-"*50)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(data_salary, data_age, on='id', how='inner'))

print("-"*50)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([data_salary, data_age]))


print("-"*50)

# 9. DELETE FROM table1 WHERE id=10;
print(data_age[data_age["id"] == 10])
print(data_age['id'].count())
print("*" * 50)
data_age = data_age[data_age["id"] != 10]
print(data_age[data_age["id"] == 10])
print(data_age['id'].count())

print("-"*50)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(data_age.head())
print("*" * 50)
del data_age['gender']
print(data_age.head())