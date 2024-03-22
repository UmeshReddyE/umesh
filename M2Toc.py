import re

# Define the productions
productions = {
    'S': ['A'],
    'A': ['0BC'],
    'B': ['0BD','1B', '€'],
    'D': ['1DD','€'],
    'C': ['1'],
}

# Define the terminals and non-terminals
terminals = ['0', '1']
non_terminals = ['S', 'A', 'B','C','D']

# Define the start symbol
start_symbol = 'S'

# Define a function to generate the CFG
def generate_cfg(productions, terminals, non_terminals, start_symbol):
    # Generate the rules
    rules = []
    for non_terminal in non_terminals:
        for production in productions[non_terminal]:
            rule = non_terminal + ' -> '
            for symbol in production:
                if symbol in terminals or symbol == '€':
                    rule += symbol
                else:
                    rule += symbol + ' '
            rules.append(rule)
    
    # Add the start symbol to the rules
    rules.insert(0, start_symbol + ' -> ' + productions[start_symbol][0])
    
    # Return the CFG
    return '\n'.join(rules)

# Generate the CFG
cfg = generate_cfg(productions, terminals, non_terminals, start_symbol)

# Print the CFG
print(cfg)
