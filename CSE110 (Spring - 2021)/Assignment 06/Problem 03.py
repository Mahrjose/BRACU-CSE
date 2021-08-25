def foo_moo(num):
    if num % 2 == 0 and num % 3 == 0:
        return "FooMoo"
    elif num % 3 == 0:
        return "Moo"
    elif num % 2 == 0:
        return "Foo"
    else:
        return "Boo"


# Function Call
print(foo_moo(5))
print(foo_moo(4))
print(foo_moo(6))
