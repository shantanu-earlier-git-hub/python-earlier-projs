def display(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


@display
def hello():
    print("Hello World")


def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result

    return wrapper


@decorator_name
def add(a, b):
    return a + b


if __name__ == '__main__':
    # hello()
    print(add(5, 3))
