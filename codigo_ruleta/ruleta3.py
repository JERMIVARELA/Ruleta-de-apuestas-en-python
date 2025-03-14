import random

def ruleta():
    saldo = 100
    historial = []
    ruleta = list(range(1, 37))
    colores = {n: 'rojo' if n % 2 == 0 else 'negro' for n in ruleta}
    ganadas = 0
    perdidas = 0
    
    while saldo > 0:
        print(f"Saldo: {saldo} coins")
        print("1. Apostar por numero")
        print("2. Apostar por seccion")
        print("3. Apostar por color")
        print("4. Ver historial")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "5":
            break
        elif opcion == "4":
            print("Historial de apuestas:")
            for h in historial:
                print(f"Apostado: {h[0]}, Ganancia: {h[1]}")
            if perdidas == 0:
                print("Promedio de exito: No hay apuestas perdidas aun.")
            else:
                print(f"Promedio de exito: {ganadas / perdidas:.2f}")
        elif opcion == "1": 
            monto = int(input("Monto a apostar: "))
            if monto > saldo:
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            num = int(input("numero (1-36): "))
            resultado = random.choice(ruleta)
            color = colores[resultado]
            print(f"Resultado: {resultado} ({color})")
            ganancia = 0
            if num == resultado:
                ganancia = monto * 20
                ganadas += 1
            else:
                perdidas += 1
            saldo += ganancia - monto
            historial.append((monto, ganancia))
            print("Ganaste!" if ganancia else "Perdiste.")
        elif opcion == "2": 
            monto = int(input("Monto a apostar: "))
            if monto > saldo:
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            print("1. Seccion A (1-12)")
            print("2. Sección B (13-24)")
            print("3. Sección C (25-36)")
            sec = input("Selecciona una sección (A/B/C): ").lower()
            if sec == "a":
                rango = range(1, 13)
                nombre_seccion = "A"
            elif sec == "b":
                rango = range(13, 25)
                nombre_seccion = "B"
            elif sec == "c":
                rango = range(25, 37)
                nombre_seccion = "C"
            else:
                print("Seccion no valida.")
                continue
            resultado = random.choice(ruleta)
            color = colores[resultado]
            print(f"Resultado: {resultado} ({color})")
            ganancia = 0
            if resultado in rango:
                ganancia = monto * 5
                ganadas += 1
            else:
                perdidas += 1
            saldo += ganancia - monto
            historial.append((monto, ganancia))
            print(f"Ganaste! (Seccion {nombre_seccion})" if ganancia else "Perdiste.")
        elif opcion == "3":  
            monto = int(input("Monto a apostar: "))
            if monto > saldo:
                print("No tienes suficiente saldo para esta apuesta.")
                continue
            col = input("Color (rojo/negro): ").lower()
            resultado = random.choice(ruleta)
            color = colores[resultado]
            print(f"Resultado: {resultado} ({color})")
            ganancia = 0
            if col == color:
                ganancia = monto * 2
                ganadas += 1
            else:
                perdidas += 1
            saldo += ganancia - monto
            historial.append((monto, ganancia))
            print("Ganaste!" if ganancia else "Perdiste.")

    print(f"Saldo final :{saldo} coins")

ruleta()        
