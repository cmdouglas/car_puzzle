import itertools
DEBUG = True

def debug(msg, value):
    if DEBUG:
        print(msg + ': ' + str(value))

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
    debug('possible decks', decks)
    expected = expected_value(decks)
    debug('expected', expected)
    
    if expected <= card:
        return False
    else:
        return True
        
def result(deck):
    debug('finding best result for deck', deck)
    best = min(deck)
    card = None
    shown = []
    while(len(deck) > 1):
        card = deck.pop(0)
        debug('card', card)
        shown.append(card)
        if will_accept(card, shown):
            debug('accepting card', card)
            return card - best
        else:
            debug('rejecting card', card)
    
    card = deck.pop(0)
    debug('forced to accept card', card)
    return card - best
    
def solve():
    cards = [0, 1, 2, 3, 4]
    decks = itertools.permutations(cards)

    results = {}

    for deck in decks:
        k = tuple(deck)
        deck = list(deck)
        results[k] = result(deck)
        debug('-- ', '--')

    print(sum(results.values())/len(results))

if __name__ == '__main__':
    solve()
