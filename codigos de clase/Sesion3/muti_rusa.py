a,b,r = 37,12,0
while(a>=1):
    if a%2!=0:
        r += b
    a //=2
    b *=2

print(f"la respuesta es {r}")