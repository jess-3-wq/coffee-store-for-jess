from customer import Customer
from coffee import Coffee


dormans = Coffee("Dormans")
doubles = Coffee("doubles")


jess = Customer("Jess")
murima = Customer("Murima")


jess.create_order(latte, 4.5)
jess.create_order(mocha, 3.0)
murima.create_order(latte, 5.0)


print("Latte orders:", latte.num_orders()) 
print("Latte average price:", latte.average_price())  
print("Latte customers:", [c.name for c in latte.customers()])  

print("Jess's orders:", jess.orders())
print("Murima's coffees:", [c.name for c in murima.coffees()])
