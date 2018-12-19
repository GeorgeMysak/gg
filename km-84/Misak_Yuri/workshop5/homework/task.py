from MakeDataset import dataset

data = dataset('orders.csv')
# Які продукти купляли усі покупці?
user_products = dict()
for user in data:
    user_products[user] = set()
    for date in data[user]:
        user_products[user].update(set(data[user][date].keys()))
orders = []
for user in user_products:
        orders.append(user_products[user])
#print(orders)
products = orders[0]
for elem in orders:
    products = products.intersection(elem)
print(list(products))