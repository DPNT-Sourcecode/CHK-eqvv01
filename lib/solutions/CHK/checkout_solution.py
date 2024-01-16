

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    special_offers = {'A': [3, 130], 'B': [2, 45]}
    item_count = count_items(skus, prices)


def count_items(skus, prices):
    quantities = {}
    for item in skus:
        if item not in prices:
            # invalid input
            return -1

        # update item count
        if item in quantities:
            quantities[item] += 1
        else:
            quantities[item] = 0


def calculate_value(item_count, prices, special_offers):
    value = 0
    for key in item_count:
        if key in special_offers:
            while special_offers[key][0] <= item_count[key]:
                value += special_offers[key][1]
                item_count[key] -= special_offers[key][0]
        value += (item_count[key] * prices[key])

    return value
