"""
PROYECTO INTEGRADOR - SEMANA 8 (VERSION FINAL ESTABILIZADA)
Caso Práctico: Sistema Inteligente de Búsqueda Binaria "Adivina el Número"
Estudiante: Jonathan Javier Manrique González
"""
import time

def calcular_intento_medio(minimo, maximo):
    """Función modular pura encargada del cálculo matemático entero."""
    return (minimo + maximo) // 2

def mostrar_encabezado():
    """Despliega la presentación estética inicial del sistema."""
    print("\n" + "="*60)
    print("    SISTEMA INTERACTIVO ALGORÍTMICO: ADIVINA EL NÚMERO")
    print("="*60)
    print(" Filosofía: Optimizar el cómputo mediante Búsqueda Binaria.")
    print("-"*60)

def main():
    # Inicialización de las variables dentro del contexto de ejecución local
    minimo = 1
    maximo = 100
    intentos = 0
    respuesta = ""
    
    mostrar_encabezado()
    print(f"Piensa en un número secreto entre {minimo} y {maximo}...")
    time.sleep(1)
    
    # Bucle repetitivo principal del software
    while respuesta != "correcto":
        intento = calcular_intento_medio(minimo, maximo)
        intentos += 1
        
        print(f"\n[Intento No. {intentos}] ¿Tu número secreto es el {intento}?")
        respuesta = input("Respuesta (mayor / menor / correcto): ").strip().lower()
        
        # Estructura de validación robusta de datos de entrada
        if respuesta not in ["mayor", "menor", "correcto"]:
            print("[Alerta] Entrada inválida. Use únicamente: 'mayor', 'menor' o 'correcto'.")
            intentos -= 1  
            continue
            
        # Bloque condicional para el ajuste de límites dinámicos
        if respuesta == "mayor":
            minimo = intento + 1
        elif respuesta == "menor":
            maximo = intento - 1
            
        # Control de consistencia lógica (Protección contra pistas falsas o contradictorias)
        if minimo > maximo and respuesta != "correcto":
            print("\n[Conflicto Lógico] Los límites se han cruzado. Reiniciando márgenes...")
            minimo = 1
            maximo = 100
            intentos = 0
            time.sleep(1)
            
    # Sección de salida formal con análisis de rendimiento
    print("\n" + "="*60)
    print("         ¡SISTEMA FINALIZADO CON ÉXITO!")
    print("="*60)
    print(f" El computador localizó el número secreto: {intento}")
    print(f" Total de intentos / iteraciones realizadas: {intentos}")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()