

# noinspection PyUnusedLocal
# skus = unicode string
item_dicts = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}
def checkout(skus):
    checkout_value = item_dicts.get(skus, -1)
    return checkout_value
    




