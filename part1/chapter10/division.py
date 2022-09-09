"""
======================
@title: division
@description: 处理 ZeroDivisionError异常
@author: elijah
@date: 2022/9/7 15:39
=====================
"""

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
