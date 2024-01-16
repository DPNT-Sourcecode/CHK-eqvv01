

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    special_offers = {'A': [[5, 200], [3, 130]], 'B': [[2, 45]]}
    itemsfree_offers = {'E': [2, 2, {'B': 1}]}
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

    # check if there is an item free offer, if so update the item count accordingly
    for itemkey in item_count:
        if itemkey in itemsfree_offers:
            temp_item_count = item_count[itemkey]
            min_offer_items = itemsfree_offers[itemkey][0]
            subtract_offer_items = itemsfree_offers[itemkey][1]
            while min_offer_items <= temp_item_count:
                for offerkey, value in itemsfree_offers[itemkey][2].items():
                    if offerkey in item_count:
                        item_count[offerkey] -= value
                temp_item_count -= subtract_offer_items

    value = 0
    for key in item_count:
        if key in special_offers:
            for offer in special_offers[key]:
                while offer[0] <= item_count[key]:
                    value += offer[1]
                    item_count[key] -= offer[0]
        value += (item_count[key] * prices[key])

    return value




