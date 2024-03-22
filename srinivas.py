import nltk
grammar = nltk.CFG.fromstring("""
 S -> aAa | bBb 
 A ->  a
 B ->  b

 """)

sent = "a a a".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for p in rd_parser.parse(sent):
    print (p)

print(sent)