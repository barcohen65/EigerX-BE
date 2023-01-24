def price_check(products, productPrices, productSold, soldPrice):
    errors = 0
    numOfProducts = len(productSold)
    for i in range(numOfProducts):
        productIndex = products.index(productSold[i])
        correctPrice = productPrices[productIndex]
        if soldPrice[i] != correctPrice:
            errors += 1
    return errors