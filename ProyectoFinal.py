# Versión 2: Procesamiento Unitario de Entrada

minimo = 1
maximo = 100
intentos = 0

print("Piensa en un número secreto entre 1 y 100...")

# Cálculo del primer punto medio y aumento del contador
intento = (minimo + maximo) // 2
intentos += 1

print(f"\n[Intento No. {intentos}] ¿Tu número secreto es el {intento}?")
respuesta = input("Respuesta (mayor / menor / correcto): ").strip()

print(f">> Registro de prueba: El usuario indicó que el número es '{respuesta}'")