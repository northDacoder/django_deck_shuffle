
def get_card_list():
    suits = ['club', 'diamond', 'heart', 'spade']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append({
                'name': '{0} of {1}s'.format(rank, suit),
                'suit': suit,
                'rank': rank
            })

    return deck