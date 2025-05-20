from customer import Customer
from coffee import Coffee


dormans = Coffee("Dormans")
doubles = Coffee("doubles")


jess = Customer("Jess")
murima = Customer("Murima")


jess.create_order(dormans, 4.5)
jess.create_order(doubles, 3.0)
murima.create_order(dormans, 5.0)


print("Dormans orders:", dormans.num_orders()) 
print("Dormans average price:", dormans.average_price())  
print("Dormans customers:", [c.name for c in dormans.customers()])  

print("Jess's orders:", jess.orders())
print("Murima's coffees:", [c.name for c in murima.coffees()])
