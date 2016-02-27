print('hello world')
if 2<4:
	print("True")
else: 
	print("False") 
volume = 120
if volume < 20:
    print("Prawie nic nie slychac.")
elif 20 <= volume < 40:
    print("O, muzyka leci w tle.")
elif 40 <= volume < 60:
    print("Idealnie, moge uslyszec wszystkie detale")
elif 60 <= volume < 80:
    print("Dobre na imprezy")
elif 80 <= volume < 100:
    print("Troszeczke za glosno!")
else:
    print("Ojoj! Moje uszy! :(")

def hej(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')
hej('xyz')

def hej2(imie):
    print('Hej ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hej2(imie)
    print('Kolejna dziewczyna')