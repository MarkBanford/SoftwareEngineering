from logistics import Logistics

T1 = Logistics.delivery_method("Air")
print(T1.deliver())
T2 = Logistics.delivery_method("Sea")
print(T2.deliver())
T3 = Logistics.delivery_method("Land")
print(T3.deliver())
