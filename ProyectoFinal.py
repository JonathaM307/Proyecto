# Versión 3: Ciclo Iterativo Principal

minimo = 1
maximo = 100
intentos = 0
respuesta = ""

print("Piensa en un número secreto entre 1 y 100...")

# Bucle interactivo controlado por la respuesta de éxito
while respuesta != "correcto":
    intento = (minimo + maximo) // 2
    intentos += 1
    
    print(f"\n[Intento No. {intentos}] ¿Tu número secreto es el {intento}?")
    respuesta = input("Respuesta (mayor / menor / correcto): ").strip()

print(f"\n[Éxito] El computador ha finalizado el ciclo en {intentos} intentos.")