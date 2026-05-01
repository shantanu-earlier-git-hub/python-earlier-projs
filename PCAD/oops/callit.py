from oops.Display import Display
from oops.rectangle import Rectangle

display = Display(name="display", age=100)
display.display()

cals = Rectangle(width=10, height=20)
print(cals.area())
print(cals.perimeter())
