from openpyxl import Workbook

# 创建一个Workbook对象，这将会创建一个Excel文件
wb = Workbook()

# 激活当前工作表
ws = wb.active

# 改变工作表的标题
ws.title = "MySheet"

# 在单元格A1中写入数据
ws['A1'] = "Hello, World!"

# 保存Excel文件
wb.save("example.xlsx")
