

# noinspection PyUnusedLocal
# skus = unicode string

# dictionaty to store SKUs
skus_dict = {
    "A": { "price": 50, "offers": "3A for 130"},
    "B": { "price": 30, "offers": "2A for 45"},
    "C": { "price": 20},
    "D": { "price": 15}
}


def checkout(skus):
    # Initialize total checkout value to zero 
    total_checkout_value = 0
    # loop through each skus to get their price
    for item in skus:
        try:
            skus_dict[item]
        # Check for invalid entry and return -1
        except KeyError:
            return -1
        # Add each sku price to total checkout
        total_checkout_value += skus_dict[item]
    #  return total checkout
    return total_checkout_value
    




