# Versión 5: Filtrado de Datos y Validación de Errores

minimo = 1
maximo = 100
intentos = 0
respuesta = ""

print("Piensa en un número secreto entre 1 y 100...")

while respuesta != "correcto":
    intento = (minimo + maximo) // 2
    intentos += 1
    
    print(f"\n[Intento No. {intentos}] ¿Tu número secreto es el {intento}?")
    # Normalización del texto para evitar fallas por mayúsculas o espacios extra
    respuesta = input("Respuesta (mayor / menor / correcto): ").strip().lower()
    
    # Compuerta de validación lógica contra entradas inválidas
    if respuesta not in ["mayor", "menor", "correcto"]:
        print("[Alerta] Entrada no válida. Por favor, digite exactamente 'mayor', 'menor' o 'correcto'.")
        intentos -= 1  # No se cuenta la iteración debido al fallo de entrada
        continue
    
    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1

print(f"\nSistema cerrado. Solución encontrada con {intentos} intentos.")