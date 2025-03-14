
#Juego de Ruleta Simulado

#Este programa permite a un usuario apostar en una ruleta virtual. 
#El jugador puede elegir entre diferentes tipos de apuestas y ver su historial.

#Características:
#- Apostar por numero especifico.
#- Apostar por sección.
#- Apostar por color.
#- Ver historial de apuestas.

#El juego finaliza cuando el saldo del jugador es 0 o cuando elige salir.5
#dependencias : 
#-se utiliza el modulo " random" para generar valores aleatorios, simulando el diro de la ruleta
#- no se requirio de paquetes externos

import random  # Importamos el módulo random para generar números aleatorios

def ruleta():
    
    #Función principal del juego de ruleta.
    #Inicializa el saldo del jugador y permite realizar diferentes tipos de apuestas.
    #gestiona el historial de apuestas
    #controla las condiciones para finalizar el juego .

    saldo = 100  # tipo (int) Saldo inicial del jugador aqui solo controlamos la cantidad con la que el jugador inicia 
    historial = []  # creamos una Lista vacia  para registrar despues las apuestas realizadas
    ruleta = list(range(1, 37))  # generamos una secuencia de numeros de 1 a 36 excluyendo a 37 Números disponibles en la ruleta :(1-36)
    #list(range(x,b)) convierte nuestra secuencia en una lista explicita de numeros .


    # Diccionario que asigna un color a cada número (pares = rojo, impares = negro)
    colores = {n: 'rojo' if n % 2 == 0 else 'negro' for n in ruleta}  #creamos un diccionario (colores) donde cada numero (n) de la lista ruleta es una clave 
    #su valor asociado es rojo si n es par (divisible por dos sin residuo ) su valor es negro si n es impar 
    #basicamente signamos un color  a cada numero como en una ruleta real donde cada par es rojo y los negros impares.


    ganadas = 0  # aqui se almacenan la cantidad de veces que el jugador a ganado (ganadas) o perdido (perdidas )
    perdidas = 0  #la funcion es llevar un registro del rendimiento del jugador permitiendo calular posteriormente la tasa de exito que tendra el jugador en sus apuestas 
    # se utiliza despues cada que el jugador gana o pierde actualizandose 

    
    while saldo > 0:  # El juego continúa mientras el jugador tenga saldo, si no tiene saldo entonces el juego acaba 
         # Muestra el menú de opciones disponibles, la variable saldo  es una variable que se modifica dinamicamente con cada apuesta ganada o  perdida 
        print(f"Saldo: {saldo} coins")       # muestra al jugador su saldo actual 
        print("1. Apostar por número")       # dependiendo de que seleccione el juagdor aqui el flujo del programa cambia 
        print("2. Apostar por sección")
        print("3. Apostar por color")
        print("4. Ver historial")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")# Solicita al usuario que ingrese una opción y la almacena en la variable 'opcion

        
        if opcion == "5":
            break  #  si el usuario selecciona 5 el juego acaba debido a la sentencia (break) el programa se deja de ejecutar y muestra el saldo final antes de cerrar 
        elif opcion == "4":
            # Muestra el historial de apuestas donde (historial) es una lisat de tuplas (monto,ganacia) deonde: h[0] representa el monto apostado en una ronda /h[1] es la ganacia optenida en esa apuesta 
            print("Historial de apuestas:")
            for h in historial:  # Recorre la lista de historial y muestra cada apuesta realizada con el bucle for 
                print(f"Apostado: {h[0]}, Ganancia: {h[1]}")
            if perdidas == 0: # si no hemos apostado y perdido   indica que no hay apuestas aun 
                print("Promedio de éxito: No hay apuestas perdidas aún.")
            else:
                print(f"Promedio de éxito: {ganadas / perdidas:.2f}") # si tenemos apuestas muestra el " promedio de exito " se utilizo la funcion .2f que formatea a dos decimales 
        elif opcion == "1":  
            # Apuesta por número específico
            monto = int(input("Monto a apostar: "))  # Solicita el monto de la apuesta y lo convierte a entero
            if monto > saldo:  # Verifica si el usuario tiene suficiente saldo
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            num = int(input("Número (1-36): "))
            resultado = random.choice(ruleta)  # Se genera un número aleatorio
            color = colores[resultado]  # Se obtiene el color del número generado la variable color almacena el color correspondiente al numero que salio en la ruleta 
            print(f"Resultado: {resultado} ({color})")
            ganancia = 0  # iniciamos una variable llamada ganacia donde se asume que la ganancia es cero hasta que verifiquemos si la respuesta es acertada 
            if num == resultado:
                ganancia = monto * 20  # Gana 20 veces la apuesta si acierta
                ganadas += 1
            else:
                perdidas += 1
            saldo += ganancia - monto  # Se actualiza el saldo
            historial.append((monto, ganancia))  # Se guarda en el historial
            print("Ganaste!" if ganancia else "Perdiste.")
        elif opcion == "2":  
            # Apuesta por sección
            monto = int(input("Monto a apostar: "))
            if monto > saldo: # Verifica si el usuario tiene suficiente saldo
                print("No tienes suficiente saldo para esta apuesta.")
                continue # Vuelve al inicio del bucle
                # Muestra las secciones disponibles para aposta
            print("1. Sección A (1-12)")
            print("2. Sección B (13-24)")
            print("3. Sección C (25-36)")
             #Solicita la sección elegida y la convierte a minúsculas para evitar errores por mayúsculas/minúsculas  
            sec = input("Selecciona una sección (A/B/C): ").lower()
            
            if sec == "a":
                rango = range(1, 13)  # Define el rango de la sección A
                nombre_seccion = "A" # asignamos el nombre de la seccion dentro de (sec) para poder mostrar despues cada seccion 
            elif sec == "b":
                rango = range(13, 25)  # Define el rango de la sección y la nombra  B
                nombre_seccion = "B"
            elif sec == "c":
                rango = range(25, 37)  # Define el rango de la sección  y la nombra C
                nombre_seccion = "C"
            else:
                print("Sección no válida.") # se ejecuta cuando el usuario ingresa un opcion incorrecta al elegir una seccion e informa que la entrada no es valida 
                continue  #continue es una palabra clave  en python que hace que el programa regrese al while, omitiendo cualquiero codigo que venga despues de este continue 
                # basicamente evita que el programa siga ejecutando el codigo ya que no es una opcion valida la que se ingreso          
                
                 
            resultado = random.choice(ruleta)  # Se genera un número aleatorio
            color = colores[resultado]  # Se obtiene el color del número generado/ la variable color almacena el color correspondiente al numero que salio en la ruleta 
            #(colores) es el diccionario que asigna un color a  cada numero y color = colores[resultado] obtiene el color del numero luego color se usa para mostrar el resultado y validar la respuesta por color 
            print(f"Resultado: {resultado} ({color})") # (resultado ) resultado es el numero aleatorio que genero la ruleta 
            ganancia = 0 # iniciamos una variable llamada ganacia donde se asume que la ganancia es cero hasta que verifiquemos si la respuesta es acertada 
            if resultado in rango:    #aqui se verifica si el numero aleatorio generado (resultado) esta dentro del rango de numeros que antes habiamos definido 
                ganancia = monto * 5  # Gana 5 veces la apuesta si acierta
                ganadas += 1  #si el jugador gana se incrementa el contador en 1  #el programa sabe que seccion escogimos ya que esa respuesta se guarda en la variable (sec)
            else:
                perdidas += 1 #si no gana (perdidas) se incrementa en 1 
            saldo += ganancia - monto  # Se actualiza el saldo del jugador (restando el monto apostado y sumando la ganancia obtenida  )
            historial.append((monto, ganancia))  # Se agrega un registro al historial en forma de tupla (monto,ganacia) esto es un seguimiento de cada apuesta que se realiza 
            print(f"Ganaste! (Sección {nombre_seccion})" if ganancia else "Perdiste.") #si ganancia tiene un valor mayor a cero entonces 
        elif opcion == "3":  
            # Apuesta por color si el usuario escoge 3 
            monto = int(input("Monto a apostar: "))  # Solicita el monto de la apuesta
            if monto > saldo: # si el monto es mayor al saldo disponible salta un mensaje de que no tiene saldo suficiente 
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            col = input("Color (rojo/negro): ").lower()  # Solicita el color a apostar #.lower() hace que la entrada se convierta en minusculas para evitar problemas 
            resultado = random.choice(ruleta)  # Se genera un número aleatorio
            color = colores[resultado]  # Se obtiene el color del número generado
            print(f"Resultado: {resultado} ({color})")  # Se muestra el resultado
            ganancia = 0  # Inicializa la ganancia en 0
            if col == color:
                ganancia = monto * 2  # Si acierta, gana el doble de la apuesta
                ganadas += 1  # Aumenta el contador de apuestas ganadas
            else:
                perdidas += 1  # Aumenta el contador de apuestas perdidas
            saldo += ganancia - monto  # Se actualiza el saldo restando la apuesta y sumando la ganancia
            historial.append((monto, ganancia))  # Se registra la apuesta en el historial
            print("Ganaste!" if ganancia else "Perdiste.")  # Se muestra el resultado
    
    print(f"Saldo final: {saldo} coins")  # Se muestra el saldo final al terminar el juego


ruleta()  # Se ejecuta el juego
