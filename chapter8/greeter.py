def greet_user():
    """ 显示简单的问候语 """
    print("Hello!")


def favorite_book(name='bible'):
    print("One of my favorite books is " + name.title())


favorite_book("Alice in Wonderland")
favorite_book()