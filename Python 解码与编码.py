# 11:18 PM, Feb 12th, 2018 @ home, Shangyu
# Python 解码与编码

# ASCII
# Unicode
# UTF-8/UTF-16/UTF-32/GBK

str = '代码 code'
print()
print("'"+str+"'" + '的各种编码')
print()
print('UTF-8编码')
print(str.encode('utf-8'))
print()
print('UTF-16编码')
print(str.encode('utf-16'))
print()
print('UTF-32编码')
print(str.encode('utf-32'))
print()
print('GBK编码')
print(str.encode('gbk'))
print()

print("'"+str+"'" + '字节流的各种解码')
print()
code = str.encode('utf-8')
print(code)
print('UTF-8解码:' + code.decode('utf-8'))
print()
code = str.encode('utf-16')
print(code)
print('UTF-16解码:' + code.decode('utf-16'))
print()
code = str.encode('utf-32')
print(code)
print('UTF-32解码:' + code.decode('utf-32'))
print()
code = str.encode('gbk')
print(code)
print('GBK解码:' + code.decode('gbk'))
print()
