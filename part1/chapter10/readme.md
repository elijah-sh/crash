## chapter10 文件和异常



## 文件和异常

### 1、从文件中读取数据



file_reader.py

```python
with open('./../files/pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)
```



> open() 打开文件 接受一个参数 要打开的文件名称
>
> close() 关闭文件，python会再合适的时间自动将其关闭



逐行读取

```python
with open('./../files/pi_digits.txt') as file_object:
    # content = file_object.read()
    # print(content)
    # print(content.strip())
    for line in file_object:
        print(line)
        # print(line.strip())
```



使用 print(line.strip()) 去除空格



使用文件内容 pi_string.py

```python
filename = './../files/pi_digits.txt'


with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
    
```



>  strip() 删除空格
>
> rstrip() 删除左边空格



### 2、写入文件



write_message.py

```python
filename = './../files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")
```



open()  第一个参数 文件名， 

第二个参数 'w' 以写入模式打开这个文件，可指定读取模式('r'), 写入模式('w'), 附件模式('a'), h或读取写入文件的模式('r+')。如果没有指定模式默认只读模式打开文件。



写入多行 并换行

```python
filename = './../files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```





### 3、异常



division.py

```python
print("Give me two numbers, and I`ll divide them.")
print("Enter 'q to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can`t divide by zero!")
    else:
        print(answer)
```

try except 避免程序崩溃

else 执行没有异常的代码块

pass 使代码继续执行



### 4、储存数据

### 

使用json.dupm() 和json.load()

函数json.dump() 接受两个实参 ：要储存的数据以及可用于储存数据的文件对象



将数字串写入文件

number_writer.py



```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = './../files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
```



json.load() 加载数据



保存读数用户信息



remember_me.py

```python
import json

# 如果以前储存了用户名，就加载他
# 否则，就提醒用户输入用户名并储存它

filename = './../files/username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We`ll remember you when you come back," + username + "!")
else:
    print("Welcome back, " + username + "!")
```





重构其方法



```python
import json

# 如果以前储存了用户名，就加载他
# 否则，就提醒用户输入用户名并储存它

def get_stored_username():
    """如果以前储存了用户名，就加载他"""
    filename = './../files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提醒用户输入用户名"""
    username = input("what is your name? ")
    filename = './../files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户， 并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We`ll remember you when you come back," + username + "!")

greet_user()
```
