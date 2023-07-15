from collections import OrderedDict
# noinspection PyUnusedLocal
# skus = unicode string

# Dictionary to store SKUs, prices and offers
skus_dict = {
    "A": { "price": 50, "offer": {"discount": [(3, 130), (5, 200)]}},
    "B": { "price": 30, "offer": {"discount": [(2, 45)]}},
    "C": { "price": 20},
    "D": { "price": 15},
    "E": { "price": 40 , "offer": {"free": [(2, "B")]}},
    "F": { "price": 10 , "offer": {"free": [(2, "F")]}},
    "G": { "price": 20},
    "H": { "price": 10, "offer": {"discount": [(5, 45), (10, 80)]}},
    "I": { "price": 35},
    "J": { "price": 60},
    "K": { "price": 70, "offer": {"discount": [(2, 120)]}},
    "L": { "price": 90},
    "M": { "price": 15},
    "N": { "price": 40, "offer": {"free": [(3, "M")]}},
    "O": { "price": 10},
    "P": { "price": 50, "offer": {"discount": [(5, 200)]}},
    "Q": { "price": 30, "offer": {"discount": [(3, 80)]}},
    "R": { "price": 50, "offer": {"free": [(3, "Q")]}},
    "S": { "price": 20, "offer": {"any_group_items": [(3, 45)]}},
    "T": { "price": 20, "offer": {"any_group_items": [(3, 45)]}},
    "U": { "price": 40, "offer": {"free": [(3, "U")]}},
    "V": { "price": 50, "offer": {"discount": [(2, 90), (3, 130)]}},
    "W": { "price": 20},
    "X": { "price": 17, "offer": {"any_group_items": [(3, 45)]}},
    "Y": { "price": 20, "offer": {"any_group_items": [(3, 45)]}},
    "Z": { "price": 21, "offer": {"any_group_items": [(3, 45)]}},
}

double_discount_items = ["A", "H", "V"]
single_discount_items = ["B", "K", "P", "Q"]
free_discount_items = ["E", "F", "N", "R", "U"]
any_three_offer_items = ["S", "T", "X", "Y", "Z"]


def get_double_offer_price(item, quantity):
    offer_price = 0
    item_discount_price = skus_dict[item]["offer"].get("discount")
    highest_discount = item_discount_price[1][0]
    highest_discount_price = item_discount_price[1][1]
    least_discount = item_discount_price[0][0]
    least_discount_price = item_discount_price[0][1]
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
        offer, leftover = divmod(quantity, discount)
        offer_price += (offer * discount_price) + (leftover * skus_dict[item]["price"])
    else:
        offer_price = quantity * skus_dict[item]["price"]
    return offer_price

def get_any_three_offer_price(item, item_details):
    if item in any_three_offer_items:
        quantity = item_details[item]
        any_three_offer_quantity += quantity
        print(any_three_offer_quantity)
        if any_three_offer_quantity == 3:
            offer_price = get_any_three_offer_price(item, quantity)
            print("yo", offer_price)
        total_checkout_value += offer_price
        print(any_three_offer_quantity)

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

    return total_checkout_value

def update_checkout_with_free_offers(item_details):
    for item in item_details:
        if item in free_discount_items:
            checkout_item_quantity = item_details.get(item, 0)
            free_offer_details = skus_dict[item]["offer"].get("free", 0)
            free_item_quantity = free_offer_details[0][0]
            free_item = free_offer_details[0][1]
            quantity_free_item_in_checkout = item_details.get(free_item, 0)
            if item == free_item:
                if checkout_item_quantity >= free_item_quantity + 1:
                    offer = checkout_item_quantity // (free_item_quantity +1)
                    if checkout_item_quantity >= offer:
                            item_details[item] = item_details[item] - offer
            else:
                if checkout_item_quantity >= free_item_quantity:
                    offer = checkout_item_quantity // free_item_quantity
                    if quantity_free_item_in_checkout >= offer:
                        item_details[free_item] = item_details[free_item] - offer
    return item_details




def checkout(skus):
    # Initialize total checkout value to zero
    total_checkout_value = 0
    any_three_offer_quantity = 0
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
    
    # Calculate free offer after item purchase
    item_details = update_checkout_with_free_offers(item_details)

    # extract group items dict
    group_of_three =  {k: v for k, v in item_details.items() if k in any_three_offer_items}
    print(set(item_details) - set(group_of_three))



    # Calculate total checkout value
    for item in item_details:
        item_offer = skus_dict[item].get("offer")
        # Calculate checkout of discounted items
        if item_offer:
            if item_offer.get("discount"):
                total_checkout_value += calculate_item_price(item, item_details)
            elif item_offer.get("any_group_items"):
                quantity = item_details[item]
                any_three_offer_quantity += quantity
                print(any_three_offer_quantity)
                if any_three_offer_quantity == 3:
                    total_checkout_value += 45
                print(any_three_offer_quantity)
                total_checkout_value += get_any_three_offer_price(item, item_details)
            else:
                total_checkout_value += item_details[item] * skus_dict[item]["price"]
        else:
            total_checkout_value += item_details[item] * skus_dict[item]["price"]
    
    return total_checkout_value


