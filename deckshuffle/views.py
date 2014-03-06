from django.shortcuts import render_to_response, render
from deckshuffle.utils import get_card_list

def card_list(request):
    deck = get_card_list()

    data = {
        "deck":deck,
    }

    response = render_to_response(
        "cards.html",
        data
    )

    return response


def inheritance(request):
    data = {}
    return render(request, 'inheritance.html', data)

def inheritance2(request):
    data = {}
    return render(request, 'inheritance2.html', data)

def specific_cards(request):
    cards = get_card_list()
    data = {
        "deck":cards,
    }
    return render(request, 'specific_cards.html', data)

def two_cards(request):
    cards = get_card_list()
    data = {
        "deck":cards,
    }
    return render(request, 'two_cards.html', data)
