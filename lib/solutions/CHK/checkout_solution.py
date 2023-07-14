

# noinspection PyUnusedLocal
# skus = unicode string

# dictionaty to store SKUs
skus_dict = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
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
    



