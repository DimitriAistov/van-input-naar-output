ticket = 7.45
vip = 0.37

personen = float(input('Hoeveel personen? '))
tijd = float(input('Hoelang? '))
tijdvip = tijd * vip

prijs = ticket + tijdvip * personen

print('Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar ' + str(prijs) + ' euro')