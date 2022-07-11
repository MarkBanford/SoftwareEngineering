from value import Value
from add import Add
from sub import Sub

A = Value(1)
B = Value(2)
C = Value(5)

print(Add(A, B))
print(Sub(C, A))
print(Sub(Add(C, B), A))
