# Resuelva cada uno de los siguientes ejercicios propuestos, puede hacer uso de listas, ciclos y funciones.
# No utilice funciones propias de python como min(), max() o librerías externas.
datos_str = input("Introduzca sus lista de números, separados por una coma:  ").replace(" ", "").split(",")
datos_int = [float(datos_str) for datos_str in datos_str]
datos_int_impar, datos_int_par = [], []

for i in range(len(datos_int)):
    for k in range((len(datos_int)) - i - 1):
        if datos_int[k] > datos_int[k + 1]:
            datos_int[k], datos_int[k + 1] = datos_int[k + 1], datos_int[k]

#?##################################################!#
#?               - Funcion Extra :D -               ?#
def clasif(datos_int):
    global datos_int_impar, datos_int_par
    for i in datos_int:
        if i % 2 == 0:
            datos_int_par.append(i)
        else:
            datos_int_impar.append(i)
    return datos_int_impar, datos_int_par
#?                                                  ?#
#?##################################################?#

#?1) Programe una función que calcule la media. Debe pasar como parámetro la lista.
def media(datos_int):
    media = 0
    for i in datos_int:
        media += i
    media = media/len(datos_int)
    print(f"La media es: {media}")


#?2) Programe una función que calcule la mediana. Debe pasar como parámetro la lista.
def mediana(datos_int):
    len_datos_int = len(datos_int)
    if len_datos_int % 2 == 0:
        mediana_1 = datos_int[int(len_datos_int / 2 - 0.5)]
        mediana_2 = datos_int[int(len_datos_int / 2 + 0.5)]
        print(f"La mediana es {(mediana_1 + mediana_2) / 2}")
    else:
        mediana = datos_int[int(len_datos_int / 2 + 0.5)]
        print(f"La mediana es {mediana}")


#?3) Programe una función que calcule la moda. Debe pasar como parámetro la lista
def moda_func(datos_int):
    moda_dict = {}
    max_dato = 0
    max_moda = 0
    for i in datos_int:
        if i in moda_dict:
            moda_dict[i] += 1
        else:
            moda_dict[i] = 1
    for i, moda in moda_dict.items():
        if moda > max_moda:
            max_moda = moda
            max_dato = i
    print(f"Su moda es {max_dato}, el cual se repite {max_moda} veces")


#?4) Programe una función que sume todos los elementos pares de una lista.
#? Debe pasar como parámetro la lista.
def suma_par(datos_int_par):
    suma_par = 0
    for i in datos_int_par:
        suma_par += i
    print(f"La suma de sus datos pares es:  {suma_par}")


#?5) Programe una función que multiplique todos los elementos impares de una lista.
#? Debe pasar como parámetro la lista.
def mult_impar(datos_int_impar):
    mult_impar = 1
    for i in datos_int_impar:
        mult_impar *= i
    print(f"La multiplicacion de sus datos impares es:  {mult_impar}")


#?6) Programe una función que elimine los elementos duplicados de una lista.
def del_dupe(datos_int):
    datos_int_nodupe = []
    for i in datos_int:
        if i not in datos_int_nodupe:
            datos_int_nodupe.append(i)
    print(f"Su nueva lista sin duplicados es:  {datos_int_nodupe}")


#?7) Programe una función que calcule la frecuencia de cada elemento de la lista.
def frec(datos_int):
    moda = {}
    for i in datos_int:
        if i in moda:
            moda[i] += 1
        else:
            moda[i] = 1
    print(f"La frecuencia de cada elemento es: {moda}")


#?8) Programe una función que ordene de menor a mayor una lista de elementos. Debepasar como parámetro la lista.
#? (No se puede invertir la lista)
def sorted_minmax(datos_int):
    for i in range(len(datos_int)):
        for k in range((len(datos_int)) - i - 1):
            if datos_int[k] > datos_int[k + 1]:
                datos_int[k], datos_int[k + 1] = datos_int[k + 1], datos_int[k]
    print(f"Lista ordenada de MENOR a MAYOR es:  {datos_int}")


#?9) Programe una función que ordene de mayor a menor una lista de elementos. Debepasar como parámetro la lista.
#? (No se puede invertir la lista)
def sorted_maxmin(datos_int):
    for i in range(len(datos_int)):
        for k in range(len(datos_int) - i - 1):
            if datos_int[k] < datos_int[k + 1]:
                datos_int[k], datos_int[k + 1] = datos_int[k + 1], datos_int[k]
    print(f"Lista ordenada de MAYOR a MENOR es:  {datos_int}")



clasif(datos_int)
media(datos_int)
mediana(datos_int)
moda_func(datos_int)
suma_par(datos_int_par)
mult_impar(datos_int_impar)
del_dupe(datos_int)
frec(datos_int)
sorted_minmax(datos_int)
sorted_maxmin(datos_int)


#?10) Realice una investigación sobre las tuplas
#?    a) ¿Qué son?
#*       En Python, una tupla es un tipo de dato que se utiliza para almacenar un conjunto de valores de diferentes tipos.
#*       Se trata de una estructura de datos inmutable, lo que significa que una vez que se crea una tupla,
#*       no se puede modificar su contenido.
#?    b) ¿Para qué sirven?
#*       Una tupla es útil en Python cuando se necesita almacenar un conjunto de valores de diferentes tipos de forma inmutable,
#*       es decir, que no se puedan modificar una vez creados. A diferencia de las listas, que son mutables y se pueden modificar
#*       sus elementos, las tuplas no pueden ser alteradas una vez ya creadas.
#?    c) Realice 3 ejercicios y describa el funcionamiento del código

"""
#TODO#  Ejercicio 1)
comp_transferencia = ("Elliott", "Mardones", "Santander", "$1.000.000", "29/12/2024")    #* Tupla
comp_transferencia_ = ["Elliott", "Mardones", "Santander", "$1.000.000", "29/12/2024"]   #! Lista
nombre, apellido, banco, monto, fecha = comp_transferencia

print(f"Nombre:  {nombre}")
print("Apellido:  {}").format(apellido)
print("Banco:  %d" % (banco))
print('Monto:' + " " + monto)
print("Fecha:",  (fecha))

#TODO# Ejercicio 2)
carnet = ("Elliott", "De las mercedes", "Mardones", "Rojas", "12,345,678-k", "12/3/4567", "123.456.789", "21/4/3765")
name1, name2, apellido1, apellito2, rut, nacimiento, nro_documento, emision_documento = carnet

print(f"Nombre:  {name1}")
print(f"Segundo Nombre:  {name2}")
print(f"Apellido Paterno:  {apellido1}")
print(f"Apellido Materno:  {apellido2}")
print(f"Rut:  {rut}")
print(f"Fecha de Nacimiento:  {nacimiento}")
print(f"Número de Documento:  {nro_documento}")
print(f"Fecha de Emisión:  {emision_documento}")

#TODO# Ejercicio 3)
registro_boleta = ("Eltit", ['manzana', 'naranja', 'plátano', 'kiwi', 'piña', 'fresa', 'melón', 'sandía', 'uva', 'limón', 'mango', 'papaya', 'cereza', 'melocotón', 'albaricoque', 'ciruela', 'pera', 'frambuesa', 'arándano', 'granada'], "40.000", "12/3/4567", "12,345,678-k")
supermercado, productos, precio, fecha_compra, rut_descuento = registro

print(f"Supermercado:  {supermercado}")
print(f"Productos Comprados:  {productos}")
print(f"Precio:  {precio}")
print(f"Fecha de Compra:  {fecha_compra}")
print(f"Rut:  {rut_descuento}")
"""
