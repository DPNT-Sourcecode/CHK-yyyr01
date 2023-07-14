

# noinspection PyUnusedLocal
# skus = unicode string
item_dicts = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}
def checkout(skus):
    # items = skus.split()
    total_value = 0
    for item in skus:
        total_value += item_dicts[item]
    checkout_value = item_dicts.get(skus, -1)
    return checkout_value
    
