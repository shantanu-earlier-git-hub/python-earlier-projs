class Rectangle():
    def __init__(self, **kwargs):
        self.__height = kwargs.get('height', 0)
        self.__width = kwargs.get('width', 0)

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * (self.__height + self.__width)
