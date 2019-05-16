from punto import Elpunto

ppunto = Elpunto(5,2)
spunto = Elpunto(1,5)

print(f'el punto 1 es {ppunto}, el segundo es {spunto}')

if ppunto == spunto:
    print('Los puntos son iguales')
else:
    print('Los puntos son diferentes')

print('El nuevo punto es', ppunto.desplazarx(4))
print('El nuevo punto es', ppunto.desplazary(4))

if ppunto == spunto:
    'No se puede hacer una pendiente por si mismo'
else:
    print(Elpunto.hallarpendiente(ppunto,spunto))


print(Elpunto.hallarvistancia(ppunto,spunto))