# Python-encode-decode
Python 中的编码与解码

#### 1:42 PM, Feb 12th, 2018

### 1. 原理说明

### Encode 和 Decode

1. 字符串通过 encode() 方法，__编码__成字节流

2. 字节流通过 decode() 方法，__解码__为字符串

3. 字符串和字节流的数据类型

   __字符串__的数据类型为 __'str'__

   ```python
   >>> str = '代码 code'
   >>> type(str)
   <class 'str'>
   ```

   __字符串编码__之后的类型为__字节流 'bytes'__

   ```python
   >>> type(str.encode('utf-8'))
   <class 'bytes'>
   ```

### 2. 使用示例

#### 1. 编码

   UTF-8 编码

   ```python
   >>> str = '代码 code'
   >>> print(str.encode('utf-8'))
   b'\xe4\xbb\xa3\xe7\xa0\x81 code'
   ```

   UTF-16 编码

   ```python
   >>> print(str.encode('utf-16'))
   b'\xff\xfe\xe3N\x01x \x00c\x00o\x00d\x00e\x00'
   ```

   UTF-32 编码

   ```python
   >>> print(str.encode('utf-32'))
   b'\xff\xfe\x00\x00\xe3N\x00\x00\x01x\x00\x00 \x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00e\x00\x00\x00'
   ```

   GBK 编码

   ```python
   >>> print(str.encode('gbk'))
   b'\xb4\xfa\xc2\xeb code'
   ```

#### 2. 解码

   设置 str 的内容为 '代码 code'

   ```python
   >>> str = '代码 code'
   ```

   UTF-8 解码

   ```python
   >>> code = str.encode('utf-8')
   >>> print(code)
   >>> print('UTF-8解码:' + code.decode('utf-8'))
   b'\xe4\xbb\xa3\xe7\xa0\x81 code'
   UTF-8解码:代码 code
   ```

   UTF-16 解码

   ```python
   >>> code = str.encode('utf-16')
   >>> print(code)
   >>> print('UTF-16解码:' + code.decode('utf-16'))
   b'\xff\xfe\xe3N\x01x \x00c\x00o\x00d\x00e\x00'
   UTF-16解码:代码 code
   ```

   UTF-32 解码

   ```python
   >>> code = str.encode('utf-32')
   >>> print(code)
   >>> print('UTF-32解码:' + code.decode('utf-32'))
   b'\xff\xfe\x00\x00\xe3N\x00\x00\x01x\x00\x00 \x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00e\x00\x00\x00'
   UTF-32解码:代码 code
   ```

   GBK 解码

   ```python
   >>> code = str.encode('gbk')
   >>> print(code)
   >>> print('GBK解码:' + code.decode('gbk'))
   b'\xb4\xfa\xc2\xeb code'
   GBK解码:代码 code
   ```

### 3. 源文件

​	查看 [Python 解码与编码.py](https://github.com/Oslomayor/Python-encode-decode/blob/master/Python%20%E8%A7%A3%E7%A0%81%E4%B8%8E%E7%BC%96%E7%A0%81.py)


