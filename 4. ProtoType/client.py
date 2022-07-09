from my_class import MyClass

obj1 = MyClass([1, [5, 6, 7], 2, 3, 4])
print(obj1)

obj2 = obj1.clone()
obj2.field[1][0] = 101

print(obj2)
print(obj1)
