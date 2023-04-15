
def apply_discount(price, percentage):
	convers = percentage/100
	priceWithDiscount = price-(convers*price)
	return priceWithDiscount


def apply_tax(price, percentage):
	convers = percentage/100
	priceWithIVA = price+(price*convers)
	return priceWithIVA


def shopping_cart(func, shoppingList):
	total = 0
	for price, percentage in shoppingList.items():
		total += func(price, percentage)

	return total


print("* Total de compra con descuento: $", shopping_cart(apply_discount, {250:30, 410:15, 584:10, 254:3}))
print()

print("* Total de compra con IVA: $", shopping_cart(apply_tax, {250:21, 410:21, 584:21, 254:21}))
	
