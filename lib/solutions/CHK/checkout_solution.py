import json
# noinspection PyUnusedLocal
# skus = unicode string

# Load JSON file
file = open("lib/solutions/CHK/skus.json")
# Dictionary to store SKUs, prices and offers
skus_dict = json.load(file)

double_discount_items = ["A", "H", "V"]
single_discount_items = ["B", "K", "P", "Q"]
free_discount_items = ["E", "F", "N", "R", "U"]
any_three_offer_items = ["S", "T", "X", "Y", "Z"]


def get_double_offer_price(item: int, quantity: str) -> int:
    """
    Calculates offer price on items with two discount offers
    Params:
        item (string): SKU item purchased
        quantity (int): quantity of item purchased
    
    Returns:
        offer_price (int): New price after offer has been applied
    """
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
    """
    Calculates offer price on items with single discount offers
    Params:
        item (string): SKU item purchased
        quantity (int): quantity of item purchased
    
    Returns:
        offer_price (int): New price after offer has been applied
    """
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
    
def get_any_three_offer_total_price(for_three):
    print(for_three)
    offer, left = divmod(len(for_three), 3)
    price = offer * 45
    if left > 0:
        for i in range(left):
            pos = (offer * 3) + i
            item = for_three[pos]["item"]
            price += skus_dict[item]["price"]
    return price


def checkout(skus):
    # Initialize total checkout value to zero
    total_checkout_value = 0
    #  Store items and quantity purchased
    item_details = {}
    for_three = []
    # loop through each skus to get their associated quantity
    for item in skus:
        # Check for invalid entry and return -1
        try:
            skus_dict[item]
        except KeyError:
            return -1
        #  increase item quantity
        if item not in any_three_offer_items:
            if item not in item_details:
                item_details[item] = 1
            else:
                item_details[item] += 1
        else:
            for_three.append({"item": item, "price": skus_dict[item]["price"]})
    sorted_three = sorted(for_three, key=lambda d: d["price"], reverse=True)
    any_three_offer_price = get_any_three_offer_total_price(sorted_three)
    # Calculate free offer on B after purchase of 2E
    item_details = update_checkout_with_free_offers(item_details)

    # Calculate total checkout value
    for item in item_details:
        item_offer = skus_dict[item].get("offer")
        # Calculate checkout of discounted items
        if item_offer:
            discounted_item = item_offer.get("discount")
            if discounted_item:
                total_checkout_value += calculate_item_price(item, item_details)
            else:
                total_checkout_value += item_details[item] * skus_dict[item]["price"]
        else:
            total_checkout_value += item_details[item] * skus_dict[item]["price"]
    
    return total_checkout_value + any_three_offer_price




