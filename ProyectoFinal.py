# Versión 4: Ajuste de Límites Algorítmicos

minimo = 1
maximo = 100
intentos = 0
respuesta = ""

print("Piensa en un número secreto entre 1 y 100...")

while respuesta != "correcto":
    intento = (minimo + maximo) // 2
    intentos += 1
    
    print(f"\n[Intento No. {intentos}] ¿Tu número secreto es el {intento}?")
    respuesta = input("Respuesta (mayor / menor / correcto): ").strip()
    
    # Estructura condicional compuesta para redefinir el espacio matemático
    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1

print(f"\n¡Logrado! El número ha sido identificado tras {intentos} intentos.")