import ttg

#Lista 1:
#Exercicio 1:
preposoicao1 = ttg.Truths(['p', 'q'], ['p and q'], ints = False)
print(preposoicao1)
preposoicao2 = ttg.Truths(['p', 'q'], ['p or q'], ints = False)
print(preposoicao2)
preposoicao3 = ttg.Truths(['p', 'q'], ['p = q'], ints = False)
print(preposoicao3)
preposoicao4 = ttg.Truths(['p', 'q'], ['p => (~q)'], ints = False)
print(preposoicao4)
preposoicao5 = ttg.Truths(['p', 'q'], ['p or (~q)'], ints = False)
print(preposoicao5)
preposoicao6 = ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints = False)
print(preposoicao6)
preposoicao7 = ttg.Truths(['p', 'q'], ['p = (~q)'], ints = False)
print(preposoicao7) 
preposoicao8 = ttg.Truths(['p', 'q'], ['(p and (~q)) => p'], ints = False)
print(preposoicao8)

#Exercicio 2:
preposoicao9 = ttg.Truths(['p', 'q'], ['(~p) and q'], ints = False)
print(preposoicao9)
preposoicao10 = ttg.Truths(['p', 'q'], ['p and (~q)'], ints = False)
print(preposoicao10)
preposoicao11 = ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints = False)
print(preposoicao11)
preposoicao12 = ttg.Truths(['p', 'q'], ['((~p) or p) and q'], ints = False)
print(preposoicao12)

#Exercicio 3:
preposoicao13 = ttg.Truths(['p', 'q'], ['(p and (~q)) => p'], ints = False)
print(preposoicao13)