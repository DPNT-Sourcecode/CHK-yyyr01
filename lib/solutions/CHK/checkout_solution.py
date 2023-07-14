

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
    if "A" in checkout_items or "B" in checkout_items:
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
    #  Store items with offers and quantity purchased
    offer_check = {}
    # loop through each skus to get their price
    for item in skus:
        # Check for invalid entry and return -1
        try:
            item_details = skus_dict[item]
        except KeyError:
            return -1
        # Check if there is offer on item
        offer_details = item_details.get("offers")
        #  Process offer on item if any
        if offer_details:
            # Split out offer details
            offer = offer_details.split(" ")
            offer_quantity = int(offer[0][0])
            offer_price = int(offer[2])
            if item not in offer_check:
                offer_check[item] = 1
            else:
                offer_check[item] += 1
                # Process if quantity is up to offer quantity
                if offer_check[item] == offer_quantity:
                    total_checkout_value += offer_price
                    del offer_check[item]
        # Add each sku price to total checkout
        else:
            total_checkout_value += skus_dict[item]["price"]
    
    for offer in offer_check:
        item = skus_dict[offer]
        total_checkout_value += offer_check[offer] * item["price"]
        
    #  return total checkout
    return total_checkout_value








