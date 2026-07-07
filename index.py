print('hello world')

# 字符串的转换
s = 'hello world'
print(s)

ss = s.upper()
print(ss)

# 字符串的拼接
s1 = 'hello'
s2 = 'world'
print(s1 + s2)

# 字符串插入
s3 = 'hello %s' % s2
print(s3)

# 字符串的格式化
s4 = 'hello {0}'.format(s2)
print(s4)

# 字符串的切片
s5 = s2[0:5]
print(s5)

# 字符串的重复
s6 = s2 * 3
print(s6)

# 字符串的查找
s7 = s2.find('l')
print(s7)

# 字符串的替换
s8 = s2.replace('l', 'L')
print(s8)

# 字符串的长度
s9 = len(s2)
print(s9)

# 字符串的比较
s10 = 'hello'
s11 = 'hello'
print(s10 == s11)

# 字符串的排序
s12 = 'hello world'
print(sorted(s12))  

# 字符串的反转
s13 = s2[::-1]
print(s13)
