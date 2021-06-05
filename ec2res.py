from math import sqrt

print("""

@@@  @@@  @@@@@@           @@@  @@@    @@@    @@@@@@            @@@@@@  
@@!  !@@ @@   @@@          @@@  @@@    @@@        @@! @@@!@@@@ @@!  @@@ 
 !@@!@!    .!!@!  @!@!@!@! @!@!@!@! @!@!@!@!@  @!!!:           @!@  !@! 
 !: :!!   !!:                   !!!    !!!        !!: !!!:!!!! !!:  !!! 
:::  ::: :.:: :::               : :    : :    ::: ::            : : ::

        creado por cholohatwhite : https://github.com/ch0l0hatwite

    calculadora de ecuaciones cuadraticas no soporta ecuaciones complejas
    
""")


vc = int(input("Ingrese el coeficiente de la variable cuadrática > "))
print("\n")
vl = int(input("Ingrese el coeficiente de la variable lineal con signo > "))
print("\n")
ti = int(input("Ingrese el término independiente > "))
print("\n")
x1= 0
x2= 0
if ((vl**2)-4*vc*ti) < 0:
  print("La solución de la ecuación es con números complejos no es posible resolverla!")
else:
  x1 = (-vl+sqrt(vl**2-(4*vc*ti)))/(2*vc)
  x2 = (-vl-sqrt(vl**2-(4*vc*ti)))/(2*vc)
  print("Las soluciones de la ecuación son:\n")
  print("x1 = ",+x1)
  print("\n")
  print("x2 = ",+x2)
