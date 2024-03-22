from sympy import symbols, Or, Implies, Not, And, satisfiable, ask
# from sympy import CNF
import cnf

# Define symbols for the suspects and variables
A, B, C, F, H, O, K, V, M = symbols('A B C F H O K V M')

# Define clauses based on the given information
clauses = [
    V,  # Victor has been murdered
    Or(A, B, C),  # Annie, Barware, and Charlie are the only suspects
    Implies(A, F),  # Annie says Barware was the victim's friend
    Implies(C, Not(H)),  # Charlie hated the victim
    Implies(B, And(O, Not(K))),  # Barware was out of town and didn't know the victim
    Implies(C, And(A, B))  # Charlie saw Annie and Barware with the victim
]

# Add the negation of 'There is no murderer' to be proven
clauses.append(Not(M))

# Convert clauses to Conjunctive Normal Form (CNF)
cnf_clauses = cnf(And(*clauses))

# Use resolution to infer conclusions
conclusions = cnf_clauses.inference()

# Print the derived conclusions
if ask(satisfiable(conclusions)):
    print("There is a murderer.")
    # Find the identity of the murderer by checking satisfiability
    model = satisfiable(cnf_clauses, all_models=True)
    for m in model:
        if m[M]:
            print("The murderer is:", m)
else:
    print("No murderer found.")
