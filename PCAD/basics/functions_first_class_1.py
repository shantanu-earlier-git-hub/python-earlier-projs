def greet(name):
    return f"Hello {name}"


def func(f, v):
    return f(v)

ref_greet = greet
print(ref_greet("Bob"))


print(func(greet, "Mike"))