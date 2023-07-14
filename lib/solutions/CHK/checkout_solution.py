

# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offers": {"discount": [(5, 200), (3, 130)]}},
    "B": { "price": 30, "offers": {"discount": [(2, 45)]}},
    "C": { "price": 20},
    "D": { "price": 15},
    "E": { "price": 40 , "offers": {"free": {"quantity": 2, "free_item": "B"}}},
    "F": { "price": 10 , "offers": "2F get one F free"}
}

# Had to re-write this to make room for new requirement 


def checkout(skus):
    # Initialize total checkout value to zero
    total_checkout_value = 0
    #  Store items and quantity purchased
    item_details = {}
    # loop through each skus to get their associated quantity
    for item in skus:
        # Check for invalid entry and return -1
        try:
            skus_dict[item]
        except KeyError:
            return -1
        #  increase item quantity
        if item not in item_details:
            item_details[item] = 1
        else:
            item_details[item] += 1
    
    # Calculate free offer on B after purchase of 2E
    quantity_of_E = item_details.get("E", 0)
    quantity_of_B = item_details.get("B", 0)
    if quantity_of_E >= 2:
        offer = quantity_of_E // 2
        if quantity_of_B >= offer:
                item_details["B"] = item_details["B"] - offer

    # Calculate free offer on F after purchase of 2F
    quantity_of_F = item_details.get("F", 0)
    if quantity_of_F >= 3:
        offer = quantity_of_F // 3
        if quantity_of_F >= offer:
                item_details["F"] = item_details["F"] - offer

    # Calculate total checkout value
    for item in item_details:
        offer_price = 0
        if item == "A":
            quantity = item_details[item]
            if quantity >= 5:
                offer, leftover = divmod(quantity, 5)
                offer_price += offer * 200
                if leftover >= 3:
                    offer, leftover = divmod(leftover, 3)
                    offer_price += (offer * 130) + leftover * skus_dict[item]["price"]
                else:
                    offer_price += leftover * skus_dict[item]["price"]
            elif quantity >= 3:
                offer, leftover = divmod(quantity, 3)
                offer_price += (offer * 130) + (leftover * skus_dict[item]["price"])
            else:
                offer_price = item_details[item] * skus_dict[item]["price"]
            total_checkout_value += offer_price
        elif item == "B":
            quantity = item_details[item]
            if quantity >= 2:
                offer, leftover = divmod(quantity, 2)
                offer_price += (offer * 45) + (leftover * skus_dict[item]["price"])
            else:
                offer_price = item_details[item] * skus_dict[item]["price"]
            total_checkout_value += offer_price
        else:
            total_checkout_value += item_details[item] * skus_dict[item]["price"]
    
    return total_checkout_value

def chk_r1_checkout(skus):
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
    
    # Process items not up to offer
    for offer in offer_check:
        item = skus_dict[offer]
        total_checkout_value += offer_check[offer] * item["price"]
        
    #  return total checkout
    return total_checkout_value




