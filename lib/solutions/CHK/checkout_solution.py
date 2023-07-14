

# noinspection PyUnusedLocal
# skus = unicode string
item_dicts = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}
def checkout(skus):
    Init
    total_checkout_value = 0
    for item in skus:
        try:
            item_dicts[item]
        except KeyError:
            return -1
        total_checkout_value += item_dicts[item]
    return total_checkout_value
    

