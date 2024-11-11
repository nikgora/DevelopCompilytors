def find_nonproductive_nonterminals(grammar, terminals):
    productive = set()
    changes = True

    while changes:
        changes = False
        for nonterminal, productions in grammar.items():
            for production in productions:
                if all(symbol in productive or symbol in terminals for symbol in production):
                    if nonterminal not in productive:
                        productive.add(nonterminal)
                        changes = True

    nonproductive = set(grammar.keys()) - productive
    return nonproductive


def find_unreachable_nonterminals(grammar, start_symbol, non_terminals):
    reachable = set()
    to_process = {start_symbol}

    while to_process:
        current = to_process.pop()
        if current not in reachable:
            reachable.add(current)
            for production in grammar.get(current, []):
                for symbol in production:
                    if symbol in non_terminals and symbol not in reachable:
                        to_process.add(symbol)

    unreachable = set(grammar.keys()) - reachable
    return unreachable


def find_vanishing_nonterminals(grammar):
    vanishing = set()
    changes = True

    while changes:
        changes = False
        for nonterminal, productions in grammar.items():
            for production in productions:
                if all(symbol in vanishing or symbol == "" for symbol in production):
                    if nonterminal not in vanishing:
                        vanishing.add(nonterminal)
                        changes = True

    return vanishing


# Приклад використання
terminals = {"a", "b", "c", "d", "e", "h", "i"}
non_terminals = {"S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}

grammar = {
    "S": [["A", "B"], ["C"]],
    "A": [["a", "A"], ["b"]],
    "B": [["b", "B"], []],
    "C": [["c"]],
    "D": [["d", "E"]],
    "E": [["e"]],
    "F": [["G"]],
    "G": [["H"]],
    "H": [["h", "I"]],
    "I": [["i", "J"]],
}

start_symbol = "S"

print("Nonproductive nonterminals:", find_nonproductive_nonterminals(grammar, terminals))
print("Unreachable nonterminals", find_unreachable_nonterminals(grammar, start_symbol, non_terminals))
print("Vanishing nonterminals", find_vanishing_nonterminals(grammar))
#Result:
# Nonproductive nonterminals: {'I', 'F', 'G', 'H'}
# Unreachable nonterminals {'F', 'E', 'H', 'D', 'G', 'I'}
# Vanishing nonterminals {'B'}
#
# Process finished with exit code 0
