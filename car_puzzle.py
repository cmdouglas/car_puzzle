import itertools

def possible_decks(shown):
    max_possible = min(shown) + 5
    min_possible = max(shown) - 4
    
    possible_cards = range(min_possible, max_possible)
    
    decks = []
    for i in range(0, len(possible_cards) - 4):
        deck = possible_cards[i:i+5]
        deck = sorted(list(set(deck) - set(shown)))
        decks.append(deck)
    
    return decks
    
def expected_value(decks):
    l = sum([len(d) for d in decks])
    s = sum([sum(d) for d in decks])
    
    return s / l    
    
def will_accept(card, shown):
    decks = possible_decks(shown)
    expected = expected_value(decks)
    
    if expected <= card:
        return False
    else:
        return True
        
def result(deck):
    best = min(deck)
    card = None
    shown = []
    while(len(deck) > 1):
        card = deck.pop()
        shown.append(card)
        if will_accept(card, shown):
            return card - best
    
    card = deck.pop()
    return card - best
    
cards = [0, 1, 2, 3, 4]
decks = itertools.permutations(cards)

results = []

for deck in decks:
    deck = list(deck)
    results.append(result(deck))

print(sum(results)/len(results))    