# 使用
from singleton import instance   # 模块只加载一次，instance 是全局唯一的
print(instance.name)  # 唯一实例
