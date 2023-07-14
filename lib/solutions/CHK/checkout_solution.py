from collections import OrderedDict
# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offer": {"discount": [(5, 200), (3, 130)]}},
    "B": { "price": 30, "offer": {"discount": [(2, 45)]}},
    "C": { "price": 20},
    "D": { "price": 15},
    "E": { "price": 40 , "offer": {"free": {"quantity": 2, "free_item": "B"}}},
    "F": { "price": 10 , "offer": {"free": {"quantity": 2, "free_item": "F"}}}
}

double_discount_items = ["A", "H", "V"]
single_discount_items = ["B", "K", "P", "Q"]
free_discount_items = ["E", "F", "N", "R", "U"]


def get_double_offer_price(item, quantity):
    offer_price = 0
    item_discount_price = skus_dict[item]["offer"].get("discount")
    highest_discount = item_discount_price[0][0]
    highest_discount_price = item_discount_price[0][1]
    least_discount = item_discount_price[1][0]
    least_discount_price = item_discount_price[1][1]
    if quantity >= highest_discount:
        offer, leftover = divmod(quantity, highest_discount)
        offer_price += offer * highest_discount_price
        if leftover >= least_discount:
            offer, leftover = divmod(leftover, least_discount)
            offer_price += (offer * least_discount_price) + leftover * skus_dict[item]["price"]
        else:
            offer_price += leftover * skus_dict[item]["price"]
    elif quantity >= least_discount:
        offer, leftover = divmod(quantity, least_discount)
        offer_price += (offer * least_discount_price) + (leftover * skus_dict[item]["price"])
    else:
        offer_price = quantity * skus_dict[item]["price"]
    return offer_price

def get_single_offer_price(item, quantity):
    offer_price = 0
    item_discount_price = skus_dict[item]["offer"].get("discount")
    discount = item_discount_price[0]
    discount_price = item_discount_price[1]
    


def calculate_item_price(item, item_details):
    offer_price = 0
    total_checkout_value = 0
    if item in double_discount_items:
        quantity = item_details[item]
        offer_price = get_double_offer_price("A", quantity)
        total_checkout_value += offer_price
    elif item in single_discount_items:
        quantity = item_details[item]
        if quantity >= 2:
            offer, leftover = divmod(quantity, 2)
            offer_price += (offer * 45) + (leftover * skus_dict[item]["price"])
        else:
            offer_price = item_details[item] * skus_dict[item]["price"]
        total_checkout_value += offer_price
    print(total_checkout_value)
    return total_checkout_value

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
        item_offer = skus_dict[item].get("offer")
        if item_offer:
            discounted_item = item_offer.get("discount")
            if discounted_item:
                total_checkout_value += calculate_item_price(item, item_details)
            else:
                total_checkout_value += item_details[item] * skus_dict[item]["price"]
        else:
            total_checkout_value += item_details[item] * skus_dict[item]["price"]
    
    return total_checkout_value








