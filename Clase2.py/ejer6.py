sexo="m"
edad=65
cotizaciones=800
aniosS=26

if aniosS>=25 and cotizaciones>=750:
    if (sexo=="m" and edad>=60) or(sexo=="f" and edad>=55):
        print("Usted aplica para ser jubilado")
        print("FELICITACIONES")
    else:
        print("Usted no aplica para ser jubilado") 
else:
    print("Usted no aplica para ser jubilado")           