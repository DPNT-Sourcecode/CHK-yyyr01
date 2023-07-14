

# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offers": "3A for 130"},
    "B": { "price": 30, "offers": "2A for 45"},
    "C": { "price": 20},
    "D": { "price": 15},
    "E": { "price": 40 , "offers": "2E get one B free"}
}

# def get_checkout_details():


def checkout(skus):
    # Initialize total checkout value to zero
    total_checkout_value = 0
    #  Store items with offers and quantity purchased
    item_details = {}
    # loop through each skus to get their price
    for item in skus:
        # Check for invalid entry and return -1
        try:
            skus_dict[item]
        except KeyError:
            return -1
        if item not in item_details:
            item_details[item] = 1
        else:
            item_details[item] += 1
    
    total_price = 0
    quantity_of_E = item_details.get("E", 0)
    quantity_of_B = item_details.get("B", 0)
    if quantity_of_E >= 2:
        offer, free_B = divmod(quantity_of_E, 2)
        if quantity_of_E:
            item_details["B"] = 



    for item in item_details:
        if item == "A":
            offer_price = 0
            quantity = item_details[item]
            if quantity >= 5:
                offer, leftover = divmod(quantity, 5)
                offer_price += offer * 200
                if leftover >= 3:
                    offer, leftover = divmod(leftover, 3)
                    offer_price += (offer * 130) + leftover * skus_dict[item]["price"]
                else:
                    offer_price = item_details[item] * skus_dict[item]["price"]
            elif quantity >= 3:
                offer, leftover = divmod(quantity, 3)
                offer_price += (offer * 130) + (leftover * skus_dict[item]["price"])
            else:
                offer_price = item_details[item] * skus_dict[item]["price"]
            total_price += offer_price
        elif item == "B":
            offer_price = 0
            quantity = item_details[item]
            if quantity >= 2:
                offer, leftover = divmod(quantity, 2)
                offer_price += (offer * 45) + (leftover * skus_dict[item]["price"])
            else:
                offer_price = item_details[item] * skus_dict[item]["price"]
            total_price += offer_price
        else:
            total_price += item_details[item] * skus_dict[item]["price"]
    
    return total_price



# def chk_r1_checkout(skus):
    # # Initialize total checkout value to zero
    # total_checkout_value = 0
    # #  Store items with offers and quantity purchased
    # offer_check = {}
    # # loop through each skus to get their price
    # for item in skus:
    #     # Check for invalid entry and return -1
    #     try:
    #         item_details = skus_dict[item]
    #     except KeyError:
    #         return -1
    #     # Check if there is offer on item
    #     offer_details = item_details.get("offers")
    #     #  Process offer on item if any
    #     if item == "A":

    #         # # Split out offer details
    #         # offer = offer_details.split(" ")
    #         # offer_quantity = int(offer[0][0])
    #         # offer_price = int(offer[2])
    #         # if item not in offer_check:
    #         #     offer_check[item] = 1
    #         # else:
    #         #     offer_check[item] += 1
    #         #     # Process if quantity is up to offer quantity
    #         #     if offer_check[item] == offer_quantity:
    #         #         total_checkout_value += offer_price
    #         #         del offer_check[item]
    #     # Add each sku price to total checkout
    #     else:
    #         total_checkout_value += skus_dict[item]["price"]
    
    # # Process items not up to offer
    # for offer in offer_check:
    #     item = skus_dict[offer]
    #     total_checkout_value += offer_check[offer] * item["price"]
        
    # #  return total checkout
    # return total_checkout_value








