ch = 'qul bl xmpl?'
y = len(ch)-1
x = 0

while ch[x] != 'e' and x != y:
    x = x + 1

if ch[x] == 'e':
    print('La chaîne de caractère contient au moins un "e"')
else:
    print('La chaîne de caractère ne contient pas de "e"')