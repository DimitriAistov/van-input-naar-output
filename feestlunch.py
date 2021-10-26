croissant, stokbrood = 0.39, 2.78
kortingsbon = -0.50

hoeveelheidCroissants = float(input('Hoeveel croissants wilt U? '))
hoeveelheidStokbrood = float(input('Hoeveel stokbrood wilt U? '))
hoeveelheidKortingsbonnen = float(input('Hoeveel kortingsbonnen heeft U? '))


prijs = croissant * hoeveelheidCroissants + stokbrood * hoeveelheidStokbrood + kortingsbon * hoeveelheidKortingsbonnen

print('De feestlunch kost je bij de bakker: ' + str(prijs) + ' euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')