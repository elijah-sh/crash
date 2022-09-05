def greet_user():
    """ 显示简单的问候语 """
    print("Hello!")


def favorite_bvook(name='bible'):
    print("One of my favorite books is " + name.title())

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 这是一个无限循环！

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# favorite_book("Alice in Wonderland")
# favorite_book()
