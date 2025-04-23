# Ejercicio 1: Simulacion de compuertas Logicas
# Definicion de Funciones:

# La compuerta and devuelve 1 cuando ambas entradas son 1, en caso contrario 0.
def compuerta_AND(valor_binario_1 = 0, valor_bionario_2 = 0):
    # Se multiplica el valor de las entradas, si ambas son 1 el resultado es 1, de lo contrario 0.
    return valor_binario_1 * valor_bionario_2
    
    
# La compuerta OR devuelve 1 cuando almenos una de sus entradas es 1, en caso contrario 0.
def compuerta_OR(valor_binario_1 = 0, valor_bionario_2 = 0):
    # Se suma el valor de las entradas. 
    resultado = numero_binario_1 + numero_binario_2
    # En caso de ambas entradas ser 1, el resultado debe ser un booleando, por eso se convierte en 1.
    if resultado == 2:
        resultado = 1
    return resultado


# La compuerta NOT invierte el valor de la entrada, en caso de la entrada ser 0 retorna 1, si es 1 retorna 0.
def compuerta_NOT(valor_binario_1 = 0):
    #La resta se debe a que si e numero es 0 se retorna 1, si es 1 se retorna 0.
    return 1 - valor_binario_1


# La compuerta or exclusiva retorna 1 si una de sus entradas es 1 y la otra 0, en caso contrario retorna 0.
def compuerta_or_exclusiva(valor_binario_1 = 0, valor_binario_2 = 0):
    # Se suma el resultado de las entradas.
    resultado = numero_binario_1 + numero_binario_2
    # En caso de ambas entradas ser 1, el resultado debe ser un booleano, por eso se convierte en 0.
    if resultado == 2:
        resultado = 0
    return resultado


# La funcion validar numero garantiza que el numero a ingresar es binario. 
def validar_numero_binario():
    # Se pide al usuario que ingrese por teclado un numero binario.
    numero_binario = int(input('Ingrese un numero binario (0 o 1): '))
    # Estructura repetitiva de permanencia que verifica que el numero sea binario.
    while numero_binario < 0 or numero_binario > 1:
        # Se imprime por pantalla el error.
        print('Error, el numero ingresado no es un numero binario.')
        # Se pide al usuario que ingrese por teclado un numero binario.
        numero_binario = int(input('Ingrese un numero binario (0 o 1): '))
    return numero_binario

# Programa Principal

#---------------------------------------------------------------------------------------------------------------
# Se pide al usuario que ingrese por teclado 2 numeros binarios.
numero_binario_1 = validar_numero_binario()
numero_binario_2 = validar_numero_binario()

# Se imprimen por pantalla los resultados de las operaciones indicadas con los 2 numeros binarios ingresados.
print('Resultados: ')
print(f'Compuerta AND: {numero_binario_1} AND {numero_binario_2} = {compuerta_AND(numero_binario_1, numero_binario_2)}')
print(f'Compuerta OR: {numero_binario_1} OR {numero_binario_2} = {compuerta_OR(numero_binario_1, numero_binario_2)}')
print(f'Compuerta NOT: {numero_binario_1} = {compuerta_NOT(numero_binario_1)}')
print(f'Compuerta NOT: {numero_binario_2} = {compuerta_NOT(numero_binario_2)}')
# La compuerta NAND es el resultado de invertir el valor del resultado de la compuerta AND.
print(f'Compuerta NAND: {numero_binario_1} NAND {numero_binario_2} = {compuerta_NOT(compuerta_AND(numero_binario_1, numero_binario_2))}')
# La compuerta NOR es el resultado de invertir el valor del resultado de la compuerta OR.
print(f'Compuerta NOR: {numero_binario_1} NOR {numero_binario_2} = {compuerta_NOT(compuerta_OR(numero_binario_1, numero_binario_2))}')
# La compuerta XOR es el resultado de invertir el valor del resultado de la compuerta OR EXCLUSIVA.
# La compuerta OR EXCLUSIVA retorna 1 cuando una de sus entradas es 1 y la otra 0, caso contrario retorna 0.
print(f'Compuerta XOR: {numero_binario_1} XOR {numero_binario_2} = {compuerta_NOT(compuerta_or_exclusiva(numero_binario_1, numero_binario_2))}')
