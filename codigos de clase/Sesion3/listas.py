nombres = ['alicia', 'beto', 'carlos', 'diana']
print(len(nombres))
print(nombres[3])
nombres[3] = 'eva'
print(nombres)

nombres.append("fran")
print(nombres)

for n in nombres:
    print(n, end="")
    input()

nombres.remove('beto')
print(nombres)

nombres.insert(3, 'daniel')
print(nombres)

# nombres.sort()
nombres.reverse()
print(nombres)
print('gabriela' in nombres)

nombres.clear()
print(nombres)

del nombres
# print(nombres)