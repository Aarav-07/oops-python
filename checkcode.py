# input_list=[1,2,33,4,4,4,5,5,6,7,8,8,9]
# output_set=set(input_list)
# print(output_set)

# def changeme(n):
#     num=1
#     print(num)
#     return
# num=10
# changeme(2).

def decorator(func):
    def wrapper(x, y):
        return func(x, y) * 2
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 4))
