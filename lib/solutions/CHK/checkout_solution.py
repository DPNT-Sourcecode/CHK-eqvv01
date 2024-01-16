

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    special_offers = {'A': '3 130', 'B': '2 45'}
    quantities = {}

    for item in skus:
        if item not in prices:
            return -1

        quantities[item] += 1

