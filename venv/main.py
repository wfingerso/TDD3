from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input("What is your product : ")
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount Percent (%) : ")
    repeat = Invoice().inputAnswer("Another Product? (y,n) : ")
    results = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = results
    if repeat == 'n':
        break

total_amount = Invoice().totalPurePrice(products)

print('Your total pure price is: ' + str(total_amount))
