from django import template
register = template.Library()

@register.filter
def specific_cards(deck, rank):
    """
    Will take in a deck of cards, and return all cards
    that have the rank given to us.
    """
    cards_to_return = []
    for card in deck:
        if card['rank'] == rank:
            cards_to_return.append(card)

    return cards_to_return

@register.filter
def two_cards(deck):
    """
    Will take in a deck of cards, and return two cards
    """
    return deck[0:2]

