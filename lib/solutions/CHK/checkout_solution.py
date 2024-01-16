

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    special_offers = {'A': [[5, 200], [3, 130]], 'B': [[2, 45]]}
    itemsfree_offers = {'E': {'B': 1}}
    item_count = count_items(skus, prices)

    if item_count == -1:
        # invalid input
        return -1

    checkout_value = calculate_value(item_count, prices, special_offers, itemsfree_offers)
    return checkout_value


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
            quantities[item] = 1

    return quantities


def calculate_value(item_count, prices, special_offers, itemsfree_offers):
    print(item_count)
    # check if there is an item free offer, if so update the item count accordingly
    for itemkey in item_count:
        if itemkey in itemsfree_offers:
            for offerkey, value in itemsfree_offers[itemkey].items():
                item_count[offerkey] -= value

    print(item_count)

    value = 0
    for key in item_count:
        if key in special_offers:
            while special_offers[key][0] <= item_count[key]:
                value += special_offers[key][1]
                item_count[key] -= special_offers[key][0]
        value += (item_count[key] * prices[key])

    return value
