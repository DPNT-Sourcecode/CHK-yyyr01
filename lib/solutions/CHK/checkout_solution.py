

# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offers": "3A for 130"},
    "B": { "price": 30, "offers": "2A for 45"},
    "C": { "price": 20},
    "D": { "price": 15}
}

    
def apply_offer(item, quantity):
    offer_price = 0
    offer = skus_dict[item].split(" ")
    new_price = offer[2]
    offer_quantity = offer[0].split()[0]
    if item_quantity > 
    of, rm = divmod(quantity, offer_quantity)
    
    

def checkout(skus):
    # Initialize total checkout value to zero 
    checkout_items = {}
    # loop through each skus to get their price
    for item in skus:
        try:
            item = skus_dict[item]
            if item in checkout_items:
                checkout_items["quantity"] += 1
            else:
                checkout_items["quantity"] = 1
        # Check for invalid entry and return -1
        except KeyError:
            return -1
        offer = skus_dict.get("offers"):
        if offers:
            discouted_price = apply_offer(item)
            
        # Add each sku price to total checkout
        total_checkout_value += skus_dict[item]
    #  return total checkout
    return total_checkout_value






