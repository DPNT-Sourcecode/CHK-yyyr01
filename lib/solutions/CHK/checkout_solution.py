

# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offers": "3A for 130"},
    "B": { "price": 30, "offers": "2A for 45"},
    "C": { "price": 20},
    "D": { "price": 15}
}

    
def apply_offer(checkout_items):
    if item == "A" or item == "B":
        offer_price = 0
        offer = skus_dict[item]["offers"].split(" ")
        offer_price = int(offer[2])
        offer_quantity = int(offer[0][0])
        print(offer_quantity)
        if item_quantity < offer_quantity:
            return item_quantity * skus_dict[item]["price"]
        of, rm = divmod(item_quantity, offer_quantity)
        new_price = (of * offer_price) + (rm * skus_dict[item]["price"])
        return new_price
    
    

def checkout(skus):
    # Initialize total checkout value to zero
    total_checkout_value = 0
    checkout_items = dict()
    # loop through each skus to get their price
    for item in skus:
        has_offer = False
        try:
            skus_dict[item]
        # Check for invalid entry and return -1
        except KeyError:
            return -1
        if item not in checkout_items:
            checkout_items[item] = 1
        else:
            checkout_items[item] += 1
        
        
    discounted_price = apply_offer(checkout_items)
            
        # Add each sku price to total checkout
    total_checkout_value += discounted_price
    #  return total checkout
    return total_checkout_value


