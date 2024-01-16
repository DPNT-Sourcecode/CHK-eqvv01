

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }
    special_offers = {
        'A': [[5, 200], [3, 130]], 'B': [[2, 45]], 'H': [[10, 80], [5, 45]],
        'K': [[2, 150]], 'P': [[5, 200]], 'Q': [[3, 80]], 'V': [[3, 130], [2, 90]]
    }
    itemsfree_offers = {
        'E': [2, 2, {'B': 1}], 'F': [3, 2, {'F': 1}],
        'N': [3, 3, {'M': 1}], 'R': [3, 3, {'Q': 1}],
        'U': [4, 3, {'U': 1}]
    }
    group_discount1_items = ['S', 'T', 'X', 'Y', 'Z']
    group_discount1_value = 45

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


def check_itemsfree_offers(item_count, itemsfree_offers):
    for itemkey in item_count:
        if itemkey in itemsfree_offers:

            temp_item_count = item_count[itemkey]
            min_offer_items = itemsfree_offers[itemkey][0]  # min no. of items needed in basket for offer
            subtract_offer_items = itemsfree_offers[itemkey][1]  # used to see how many times to apply the offer

            while min_offer_items <= temp_item_count:
                for offerkey, value in itemsfree_offers[itemkey][2].items():
                    if offerkey in item_count:
                        item_count[offerkey] -= value
                temp_item_count -= subtract_offer_items


def calculate_value(item_count, prices, special_offers, itemsfree_offers):

    # check if there is an item free offer, if so update the item count accordingly


    value = 0
    for key in item_count:
        if key in special_offers:
            for offer in special_offers[key]:
                while offer[0] <= item_count[key]:
                    value += offer[1]
                    item_count[key] -= offer[0]
        value += (item_count[key] * prices[key])

    return value

