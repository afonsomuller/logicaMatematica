import ttg

print('Lista 1:')
print('Exercicio 1:')
print('b)')
preposoicao1 = ttg.Truths(['p', 'q'], ['p and q'], ints = False)
print(preposoicao1)
print('c)')
preposoicao2 = ttg.Truths(['p', 'q'], ['p or q'], ints = False)
print(preposoicao2)
print('d)')
preposoicao3 = ttg.Truths(['p', 'q'], ['p = q'], ints = False)
print(preposoicao3)
print('e)')
preposoicao4 = ttg.Truths(['p', 'q'], ['p => (~q)'], ints = False)
print(preposoicao4)
print('f)')
preposoicao5 = ttg.Truths(['p', 'q'], ['p or (~q)'], ints = False)
print(preposoicao5)
print('g)')
preposoicao6 = ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints = False)
print(preposoicao6)
print('h)')
preposoicao7 = ttg.Truths(['p', 'q'], ['p = (~q)'], ints = False)
print(preposoicao7)
print('i)')
preposoicao8 = ttg.Truths(['p', 'q'], ['(p and (~q)) => p'], ints = False)
print(preposoicao8)

print('Exercicio 2:')
print('a)')
preposoicao9 = ttg.Truths(['p', 'q'], ['(~p) and q'], ints = False)
print(preposoicao9)
print('b)')
preposoicao10 = ttg.Truths(['p', 'q'], ['p and (~q)'], ints = False)
print(preposoicao10)
print('c)')
preposoicao11 = ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints = False)
print(preposoicao11)
print('d)')
preposoicao12 = ttg.Truths(['p', 'q'], ['((~p) or p) and q'], ints = False)
print(preposoicao12)

print('Exercicio 3:')
print('a)')
preposoicao13 = ttg.Truths(['p', 'q'], ['p => q'], ints = False)
print(preposoicao13)
print('c)')
preposoicao14 = ttg.Truths(['p', 'q'], ['~((~p) and (~q))'], ints = False)
print(preposoicao14)

print('Exercicio 4:')
print('a)')
preposoicao15 = ttg.Truths(['p', 'q', 'r'], ['(p or q) and (~r)'], ints = False)
print(preposoicao15)
print('b)')
preposoicao16 = ttg.Truths(['p', 'q', 'r'], ['(p and q) or (~(p and r))'], ints = False)
print(preposoicao16)
print('c)')
preposoicao17 = ttg.Truths(['p', 'r'], ['~(p and(~r))'], ints = False)
print(preposoicao17)
print('d)')
preposoicao18 = ttg.Truths(['p', 'q', 'r'], ['~((q or r) and (~p))'], ints = False)
print(preposoicao18)

print('Exercicio 5:')
print('a)')
preposoicao19 = ttg.Truths(['p', 'q', 'r'], ['~((p and r) or (~q))'], ints = False)
print(preposoicao19)
print('b)')
preposoicao20 = ttg.Truths(['p', 'q', 'r'], ['((~p) or (~q)) and r'], ints = False)
print(preposoicao20)
print('c)')
preposoicao21 = ttg.Truths(['p', 'q', 'r'], ['(~r) => (p and (~q))'], ints = False)
print(preposoicao21)
print('d)')
preposoicao22 = ttg.Truths(['p', 'q', 'r'], ['~((~p) and (~q)) and (r and p)'], ints = False)
print(preposoicao22)


print('Lista 2:')
print('Exercicio 3:')
print('a)')
preposoicao23 = ttg.Truths(['a', 'b'], ['(~a) and b'], ints = False)
print(preposoicao23)
print('b)')
preposoicao24 = ttg.Truths(['a', 'b'], ['(~b) => (a or b)'], ints = False)
print(preposoicao24)
print('c)')
preposoicao25 = ttg.Truths(['a', 'c'], ['(c or a) = (~(~c))'], ints = False)
print(preposoicao25)
print('d)')
preposoicao26 = ttg.Truths(['a', 'b'], ['a or (a => b)'], ints = False)
print(preposoicao26)
print('e)')
preposoicao27 = ttg.Truths(['a', 'c', 'd'], ['(d or (~a)) => (~c)'], ints = False)
print(preposoicao27)
print('f)')
preposoicao28 = ttg.Truths(['a', 'b', 'c'], ['~(a and b) => (~(c and b))'], ints = False)
print(preposoicao28)

print('Exercicio 4:')
print('a)')
preposoicao29 = ttg.Truths(['p', 'q'], ['~(p => ~q)'], ints = False)
print(preposoicao29)
print('b)')
preposoicao30 = ttg.Truths(['p', 'q', 'r'], ['p = ~q and r'], ints = False)
print(preposoicao30)
print('c)')
preposoicao31 = ttg.Truths(['p', 'q', 'r'], ['p => ~q and p or q = p or ~q'], ints = False)
print(preposoicao31)


print('Lista 3:')
print('Exercicio 1:')
preposoicao32 = ttg.Truths(['l', 't', 'd'], ['l and t and d'], ints = False)
print(preposoicao32)

print('Exercicio 2:')
preposoicao33 = ttg.Truths(['m', 'a'], ['m and ~a'], ints = False)
print(preposoicao33)

print('Exercicio 3:')
preposoicao34 = ttg.Truths(['a', 'b', 'r'], ['a and (b or r)'], ints = False)
print(preposoicao34)

print('Exercicio 4:')
preposoicao35 = ttg.Truths(['r', 'm', 'c'], ['r and m and ~c'], ints = False)
print(preposoicao35)

print('Exercicio 5:')
preposoicao36 = ttg.Truths(['a', 'h', 't'], ['(a and h) or (t and ~h)'], ints = False)
print(preposoicao36)