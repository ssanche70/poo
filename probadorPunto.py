from punto import Elpunto

ppunto = Elpunto(1,2)
spunto = Elpunto(2,4)

print(f'el punto 1 es {ppunto}, el segundo es {spunto}')

if ppunto == spunto:
    print('Los puntos son iguales')
else:
    print('Los puntos son diferentes')

print('El nuevo punto es', ppunto.desplazarx(4))
print('El nuevo punto es', ppunto.desplazary(4))

print(Elpunto.hallarpendiente(ppunto,spunto))