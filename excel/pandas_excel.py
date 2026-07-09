import pandas as pd

# 读取Excel文件到DataFrame
df = pd.read_excel('example.xlsx', sheet_name='MySheet')
print(df)


# 创建一个DataFrame
data = {'Name': ['John', 'Anna'], 'Age': [28, 22]}
df = pd.DataFrame(data)

# 将DataFrame写入Excel文件，不覆盖原有数据（如果需要覆盖，使用mode='w'）
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False, engine='openpyxl')