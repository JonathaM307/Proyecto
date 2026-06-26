# Proyecto Integrador: Adivina el Número

Este repositorio contiene el desarrollo del Proyecto Integrador para la asignatura **Lógica de Programación**, titulado *"El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas"*. 

El sistema implementa un algoritmo interactivo de **Búsqueda Binaria** mediante el cual el computador optimiza dinámicamente los recursos lógicos para adivinar un número secreto pensado por el usuario (entre 1 y 100) en el menor número de intentos posible.

---

## 📑 Tabla de Contenidos
- [Descripción del Problema](#-descripción-del-problema)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Historial de Desarrollo y Versiones (Commits)](#-historial-de-desarrollo-y-versiones-commits)
- [Características Técnicas Relevantes](#-características-técnicas-relevantes)
- [Instalación y Ejecución](#-instalación-y-ejecución)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)

---

## Descripción del Problema

El problema central radica en diseñar un método eficiente de búsqueda interactiva. El usuario concibe un número secreto dentro de un rango preestablecido (1 a 100) y el sistema informático provee aproximaciones sucesivas. Tras cada intento, el usuario retroalimenta al sistema con tres estados lógicos:
* `mayor`: El número secreto es más alto que el intento actual.
* `menor`: El número secreto es más bajo que el intento actual.
* `correcto`: El número ha sido identificado de manera exitosa.

### Justificación de Eficiencia
En lugar de emplear una búsqueda secuencial (complejidad lineal $O(n)$), este software aplica **Búsqueda Binaria** (complejidad logarítmica $O(\log n)$). Esto permite reducir el espacio de búsqueda exactamente a la mitad en cada iteración, logrando resolver cualquier número en un máximo teórico de 7 intentos, optimizando el tiempo de procesamiento y el uso de recursos computacionales.

---

## Arquitectura del Sistema

El software está diseñado bajo un modelo estructurado y secuencial dividido en tres niveles principales:

1. **Nivel de Entrada:** Captura los datos ingresados por consola, eliminando espacios residuales y normalizando el texto a minúsculas para mitigar errores tipográficos del usuario.
2. **Nivel de Procesamiento:** Ejecuta el cálculo matemático del punto medio entero utilizando división truncada `(minimo + maximo) // 2` y reajusta los límites numéricos dinámicamente según la pista provista.
3. **Nivel de Salida:** Despliega métricas de rendimiento, el conteo total de iteraciones lógicas realizadas y alertas en caso de que ocurran fallas lógicas o de entrada.

---

## Historial de Desarrollo y Versiones (Commits)

El software se construyó de manera incremental, aplicando metodologías ágiles de desarrollo y un estricto control de versiones en Git. La evolución se compone de las siguientes fases:

* **v1.0.0 (Commit 1):** `definir limites de busqueda e interactividad basica por consola`
  * Inicialización de variables de control y diseño del banner estético de interfaz.
* **v2.0.0 (Commit 2):** `agregar captura de entrada e intento de procesamiento secuencial`
  * Implementación del primer cálculo del punto medio y captura inicial de datos de prueba.
* **v3.0.0 (Commit 3):** `integrar bucle de control repetitivo para ejecucion continua`
  * Inclusión del ciclo repetitivo `while` controlado por condición de parada interactiva.
* **v4.0.0 (Commit 4):** `incorporar condicionales if-elif para modificacion de limites`
  * Programación de las bifurcaciones condicionales que reajustan dinámicamente los rangos de búsqueda.
* **v5.0.0 (Commit 5):** `normalizar cadenas y agregar control de excepciones para entradas invalidas`
  * Robustez de software: integración de filtros de sanidad de cadenas (`.lower()`) y compuerta lógica que ignora entradas inválidas sin penalizar el contador.
* **v6.0.0 (Commit 6):** `estructurar codigo en funciones modulares e integrar control de inconsistencias`
  * Refactorización final: separación de responsabilidades en funciones puras, protección ante contradicciones del usuario y encapsulamiento bajo el punto de entrada estándar `if __name__ == '__main__':`.

---

## Características Técnicas Relevantes

* **Estructuras Repetitivas:** Ciclo `while` continuo controlado eficientemente por estado interactivo.
* **Estructuras Condicionales Compuestas:** Lógica anidada `if-elif-else` para la toma de decisiones algorítmicas rápidas.
* **Programación Funcional Modular:** Segmentación limpia de tareas informáticas que promueve la reutilización y el mantenimiento del código.
* **Control de Consistencia:** Mecanismo de seguridad que resetea los límites automáticos en caso de que el usuario provea pistas cruzadas o contradictorias por error.
