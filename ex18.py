# Name, Variables, Functions


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    print(f"Type1: {type(arg1)}. Type2: {type(arg2)}")


def print_take_2(one, two):
    print(f"Value1: {one}, Value2: {two}")


def print_take_1(one):
    print(f"Value: {one}")


def print_none():
    print("I got nothing")


print_two(12, 'abcd')
print_take_2("Donald", 'Trump')
print_take_1("Hello")
print_none()