from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
print("\n............select any RE to perform converting RE into DFA............ \n")
print("\t\t1. a(ba)*b\n\t\t2. (a ∪ 𝑏)*a(a ∪ 𝑏)*b(a ∪ 𝑏)*a(a ∪ 𝑏)*\n\t\t3. (a ∪ ba ∪ b b)(a ∪ b)*\n\t\t4.Exit()\n")
choice=0
while choice != 4:
    choice=int(input("enter your choice :"))
    if choice==1:
        nfa1 = NFA.from_regex('a(ba)*b')
        print("\nconvert the given RE into Epsilon NFA is :\n")
        print(nfa1)
        # print(nfa1.accepts_input("abab"))
        print("\n")
        print("\nconvert the given Epsilon NFA into DFA is :\n")
        dfa = DFA.from_nfa(nfa1)  # returns an equivalent DFA
        print(dfa)
        dfa1=NFA.from_dfa(dfa)
        # print(dfa.accepts_input("abab"))
        print("\n")


    if choice==2:
        nfa1 = NFA.from_regex('(a|b)*a(a|b)*b(a|b)*a(a|b)*')
        print("\nconvert the given RE into Epsilon NFA is :\n")
        print(nfa1)
        # print(nfa1.accepts_input("aabaaa"))
        print("\n")
        print("\nconvert the given Epsilon NFA into DFA is :\n")
        dfa = DFA.from_nfa(nfa1)  # returns an equivalent DFA
        print(dfa)
        # print(dfa.accepts_input("aabaaa"))
        print("\n")

    if choice==3:
        nfa1 = NFA.from_regex('(a | ba | bb)(a | b)*')
        print("\nconvert the given RE into Epsilon NFA is :\n")
        print(nfa1)
        # print(nfa1.accepts_input("aabaaa"))
        print("\n")
        print("\nconvert the given Epsilon NFA into DFA is :\n")
        dfa = DFA.from_nfa(nfa1)  # returns an equivalent DFA
        print(dfa)
        # print(dfa.accepts_input("aabaaa")
        print("\n")
