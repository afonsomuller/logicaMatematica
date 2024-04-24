import ttg

#Lista 1:
#Exercicio 1:
#b)
preposoicao1 = ttg.Truths(['p', 'q'], ['p and q'], ints = False)
print(preposoicao1)
#c)
preposoicao2 = ttg.Truths(['p', 'q'], ['p or q'], ints = False)
print(preposoicao2)
#d)
preposoicao3 = ttg.Truths(['p', 'q'], ['p = q'], ints = False)
print(preposoicao3)
#e)
preposoicao4 = ttg.Truths(['p', 'q'], ['p => (~q)'], ints = False)
print(preposoicao4)
#f)
preposoicao5 = ttg.Truths(['p', 'q'], ['p or (~q)'], ints = False)
print(preposoicao5)
#g)
preposoicao6 = ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints = False)
print(preposoicao6)
#h)
preposoicao7 = ttg.Truths(['p', 'q'], ['p = (~q)'], ints = False)
print(preposoicao7)
#i)
preposoicao8 = ttg.Truths(['p', 'q'], ['(p and (~q)) => p'], ints = False)
print(preposoicao8)

#Exercicio 2:
#a)
preposoicao9 = ttg.Truths(['p', 'q'], ['(~p) and q'], ints = False)
print(preposoicao9)
#b)
preposoicao10 = ttg.Truths(['p', 'q'], ['p and (~q)'], ints = False)
print(preposoicao10)
#c)
preposoicao11 = ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints = False)
print(preposoicao11)
#d)
preposoicao12 = ttg.Truths(['p', 'q'], ['((~p) or p) and q'], ints = False)
print(preposoicao12)

#Exercicio 3:
#a)
preposoicao13 = ttg.Truths(['p', 'q'], ['p => q'], ints = False)
print(preposoicao13)
#c)
preposoicao14 = ttg.Truths(['p', 'q'], ['~((~p) and (~q))'], ints = False)
print(preposoicao14)

#Exercicio 4:
#a)
preposoicao15 = ttg.Truths(['p', 'q', 'r'], ['(p or q) and (~r)'], ints = False)
print(preposoicao15)
#b)
preposoicao16 = ttg.Truths(['p', 'q', 'r'], ['(p and q) or (~(p and r))'], ints = False)
print(preposoicao16)
#c)
preposoicao17 = ttg.Truths(['p', 'r'], ['~(p and(~r))'], ints = False)
print(preposoicao17)
#d)
preposoicao18 = ttg.Truths(['p', 'q', 'r'], ['~((q or r) and (~p))'], ints = False)
print(preposoicao18)

#Exercicio 5:
#a)
preposoicao19 = ttg.Truths(['p', 'q', 'r'], ['~((p and r) or (~q))'], ints = False)
print(preposoicao19)
#b)
preposoicao20 = ttg.Truths(['p', 'q', 'r'], ['((~p) or (~q)) and r'], ints = False)
print(preposoicao20)
#c)
preposoicao21 = ttg.Truths(['p', 'q', 'r'], ['(~r) => (p and (~q))'], ints = False)
print(preposoicao21)
#d)
preposoicao22 = ttg.Truths(['p', 'q', 'r'], ['~((~p) and (~q)) and (r and p)'], ints = False)
print(preposoicao22)


#Lista 2:
#Exercicio 3:
#a)
preposoicao23 = ttg.Truths(['a', 'b'], ['(~a) and b'], ints = False)
print(preposoicao23)

preposoicao24 = ttg.Truths(['a', 'b'], ['(~b) => (a or b)'], ints = False)
print(preposoicao24)
preposoicao25 = ttg.Truths(['a', 'c'], ['(c or a) = (~(~c))'], ints = False)
print(preposoicao25)
preposoicao26 = ttg.Truths(['a', 'b'], ['a or (a => b)'], ints = False)
print(preposoicao26)
preposoicao27 = ttg.Truths(['a', 'c', 'd'], ['(d or (~a)) => (~c)'], ints = False)
print(preposoicao27)
preposoicao28 = ttg.Truths(['a', 'b', 'c', 'd'], ['~(a and b) => (~(c and b))'], ints = False)
print(preposoicao28)

#Exercicio 4:
preposoicao29 = ttg.Truths(['p', 'q'], ['~(p => ~q)'], ints = False)
print(preposoicao29)
preposoicao30 = ttg.Truths(['p', 'q', 'r'], ['p = ~q and r'], ints = False)
print(preposoicao30)
preposoicao31 = ttg.Truths(['p', 'q', 'r'], ['p => ~q and p or q = p or ~q'], ints = False)
print(preposoicao31)


#Lista 3:
#Exercicio 1:
preposoicao32 = ttg.Truths(['l', 't', 'd'], ['l and t and d'], ints = False)
print(preposoicao32)

#Exercicio 2:
preposoicao33 = ttg.Truths(['m', 'a'], ['m and ~a'], ints = False)
print(preposoicao33)

#Exercicio 3:
preposoicao34 = ttg.Truths(['a', 'b', 'r'], ['a and (b or r)'], ints = False)
print(preposoicao34)

#Exercicio 4:
preposoicao35 = ttg.Truths(['r', 'm', 'c'], ['r and m and ~c'], ints = False)
print(preposoicao35)

#Exercicio 5:
preposoicao36 = ttg.Truths(['a', 'h', 't'], ['(a and h) or (t and ~h)'], ints = False)
print(preposoicao36)