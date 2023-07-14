from collections import OrderedDict
# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offer": {"discount": [(5, 200), (3, 130)]}},
    "B": { "price": 30, "offer": {"discount": [(2, 45)]}},
    "C": { "price": 20},
    "D": { "price": 15},
    "E": { "price": 40 , "offer": {"free": {"quantity": 2, "item": "B"}}},
    "F": { "price": 10 , "offer": {"free": {"quantity": 2, "item": "F"}}},
    "G": { "price": 20},
    "H": { "price": 10, "offer": {"discount": [(5, 45), (10, 80)]}},
    "I": { "price": 35},
    "J": { "price": 60},
    "K": { "price": 80, "offer": {"discount": [(2, 150)]}},
    "L": { "price": 90},
    "M": { "price": 15},
    "N": { "price": 40, "offer": {"free": {"quantity": 3, "item": "M"}}},
    "O": { "price": 10},
    "P": { "price": 50, "offer": {"discount": [(5, 200)]}},
    "Q": { "price": 30, "offer": {"discount": [(3, 80)]}},
    "R": { "price": 50, "offer": {"free": {"quantity": 3, "item": "Q"}}},
    "S": { "price": 30},
    "T": { "price": 20},
    "U": { "price": 40, "offer": {"free": {"quantity": 3, "item": "U"}}},
    "V": { "price": 50, "offer": {"discount": [(2, 90), (3, 130)]}},
    "W": { "price": 20},
    "X": { "price": 90},
    "Y": { "price": 10},
    "Z": { "price": 50},
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
    discount = item_discount_price[0][0]
    discount_price = item_discount_price[0][1]
    if quantity >= discount:
        offer, leftover = divmod(quantity, 2)
        offer_price += (offer * discount_price) + (leftover * skus_dict[item]["price"])
    else:
        offer_price = quantity * skus_dict[item]["price"]
    return offer_price



def calculate_item_price(item, item_details):
    offer_price = 0
    total_checkout_value = 0
    if item in double_discount_items:
        quantity = item_details[item]
        offer_price = get_double_offer_price(item, quantity)
        total_checkout_value += offer_price
    elif item in single_discount_items:
        quantity = item_details[item]
        offer_price = get_single_offer_price(item, quantity)
        total_checkout_value += offer_price
    print(total_checkout_value)
    return total_checkout_value

def update_checkout_with_free_offers(item_details):
    print(item_details)
    for item in item_details:
        if item in free_discount_items:
            checkout_item_quantity = item_details.get(item, 0)
            free_offer_details = skus_dict[item]["offer"].get("free", 0)
            free_item_quantity = free_offer_details.get("quantity")
            free_item = free_offer_details.get("item", 0)
            print(free_item, free_item_quantity)
            if item == free_item:
                if checkout_item_quantity >= free_item_quantity + 1:
                    offer = checkout_item_quantity // (free_item_quantity +1)
                    if checkout_item_quantity >= offer:
                            item_details[item] = item_details[item] - offer
            else:
                if checkout_item_quantity >= free_item_quantity:
                    offer = checkout_item_quantity // free_item_quantity
                    if free_item_quantity >= offer:
                            item_details[free_item] = item_details[free_item] - offer
    return item_details




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
    item_details = update_checkout_with_free_offers(item_details)
    # quantity_of_E = item_details.get("E", 0)
    # quantity_of_B = item_details.get("B", 0)
    # if quantity_of_E >= 2:
    #     offer = quantity_of_E // 2
    #     if quantity_of_B >= offer:
    #             item_details["B"] = item_details["B"] - offer

    # # Calculate free offer on F after purchase of 2F
    # quantity_of_F = item_details.get("F", 0)
    # if quantity_of_F >= 3:
    #     offer = quantity_of_F // 3
    #     if quantity_of_F >= offer:
    #             item_details["F"] = item_details["F"] - offer

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







