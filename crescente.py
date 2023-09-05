
i = range(0,100)

with open('crescente.txt','w') as arquivo:
    for numero in i:
        arquivo.write(f'{numero};')
with open('crescente.txt','r') as arquivo:
    print(arquivo.read()) 
    print(i.stop)
