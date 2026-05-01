from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'age', 'salary'])

em1 = Employee(name="name1", age=10, salary=1000)
