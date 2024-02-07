

cantidadYearsBisiesto = 0
yearInicio = int(1900)
year=(int(input("Ingrese el año que desea examinar: ")))

#Si el año no es divisible entre 4
if year % 4 != 0:
    print(year, "No es un año bisiesto")

#Si el año es divisible entre 4 pero no entre 100, por logica tampoco por 400, aunque igual se puede poner
elif year % 4 == 0 and year % 100 != 0:
    print(year, "Es un año bisiesto")

#Si el año es divisible entre 4, tambien entre 100 pero no entre 400
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print(year, "No es un año bisiesto")

#Si el año es divisible entre 4, entre 100 y tambien entre 400
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(year, "Es un año bisiesto")

#Cuantos años han pasado desde 1900 hasta el año que ingresa el usuario
yearpasados = int(year - yearInicio)


while yearInicio <= year:
    if yearInicio % 4 != 0:
        cantidadYearsBisiesto += 0

    elif yearInicio % 4 == 0 and yearInicio % 100 != 0:
        cantidadYearsBisiesto += 1

    elif yearInicio % 4 == 0 and yearInicio % 100 == 0 and yearInicio % 400 != 0:
        cantidadYearsBisiesto += 0

    elif yearInicio % 4 == 0 and yearInicio % 100 == 0 and yearInicio % 400 == 0:
        cantidadYearsBisiesto += 1

    yearInicio += 1

print("Desde 1900 hasta", year, "han pasado", yearpasados, "años, de los cuales", cantidadYearsBisiesto, "años han sido bisiesto")