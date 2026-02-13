INFORME DE PROYECTO: "IA ADIVINADORA DE ANIMALES"
Nombre del Estudiante:
José Alfredo Prieto Amarán
1. INTRODUCCIÓN

El presente proyecto consiste en el desarrollo de un programa interactivo desarrollado en Python que implementa un sistema de adivinanza basado en un árbol de decisión. La aplicación, titulada "IA Adivinadora de Animales", tiene como finalidad interactuar con el usuario a través de una serie de preguntas de opción múltiple para determinar el animal en el que está pensando.

La motivación para realizar este proyecto surge del interés por explorar cómo se pueden representar conocimientos complejos mediante estructuras de datos simples, específicamente utilizando diccionarios anidados en Python. Además, se buscó incorporar un mecanismo de aprendizaje automático básico que permita al programa ampliar su base de conocimientos cuando no logra adivinar correctamente, almacenando la información de manera persistente en un archivo externo.

El programa está diseñado para ser intuitivo y educativo, mostrando cómo la inteligencia artificial, incluso en su forma más simple, puede simular procesos de deducción y aprendizaje similares a los humanos.
2. DESARROLLO
2.1 Estructura del Proyecto

El proyecto se compone de un único archivo Python que contiene toda la lógica del programa, más un archivo JSON que funciona como base de datos persistente:

    adivinador.py (o el nombre que hayas asignado): Archivo principal que contiene el código fuente.

    animales.json: Archivo generado automáticamente que almacena el árbol de conocimiento actualizado después de cada partida.

2.2 Componentes del Código

2.2.1 Base de Conocimiento Inicial (datos_iniciales)

El corazón del programa es un gran diccionario anidado que representa un árbol de decisión. Cada nodo del árbol contiene:

    Una pregunta que se muestra al usuario.

    Un conjunto de opciones que llevan a otros nodos o a animales específicos.

La estructura comienza con la pregunta principal: "¿En qué medio vive principalmente?", con tres grandes ramas: terrestre, acuático y volador. Cada una de estas ramas se subdivide en hábitats específicos, número de patas, tipo de piel, etc., hasta llegar a nodos hoja que contienen el nombre de un animal.

Ejemplo de la estructura del árbol:
text

terrestre → desierto → 4 patas → pelaje → ¿Tiene jorobas? → Camello
                                            ↓
                                      ¿No coincide? → Coyote

2.2.2 Funciones Principales

El programa implementa dos funciones esenciales:

    guardar_datos(datos): Esta función recibe la estructura actualizada del árbol y la guarda en el archivo animales.json con formato JSON legible (indentado y con caracteres UTF-8). Incluye manejo de excepciones para evitar que el programa falle si hay problemas al escribir el archivo.

    cargar_y_jugar(): Es la función principal que orquesta toda la experiencia del juego. Su flujo de trabajo es:

        Verifica si existe un archivo animales.json con conocimientos previos; si existe, lo carga; si no, utiliza los datos_iniciales.

        Inicia un bucle que recorre el árbol mostrando preguntas y opciones.

        Detecta automáticamente cuándo se encuentra en un nivel final (donde las opciones apuntan directamente a animales).

        Procesa las respuestas numéricas del usuario y navega por el árbol.

2.2.3 Mecanismo de Aprendizaje

La característica más innovadora del programa es su capacidad de aprender. Cuando el sistema llega a un nivel final y el usuario indica que ninguna opción coincide, se activa el siguiente proceso:

    El programa muestra el animal que tenía asociado por defecto (por ejemplo, "Coyote" si se venía por la rama desierto/pelaje).

    Pregunta si ese era el animal pensado.

    Si el usuario dice que no, el programa solicita:

        El nombre del animal verdadero.

        Una característica que distinga a ese nuevo animal.

    Con esta información, el programa agrega dinámicamente una nueva rama al árbol en el nodo actual.

    Finalmente, guarda todo el árbol actualizado en el archivo JSON.

Este mecanismo permite que el programa sea más "inteligente" con cada uso, acumulando conocimiento sobre nuevos animales que no estaban en la base inicial.

2.2.4 Manejo de la Interfaz de Usuario

La interacción se realiza completamente por consola, con un diseño amigable que incluye:

    Números para seleccionar opciones fácilmente.

    Validación de entradas para evitar errores por datos incorrectos.

    Mensajes claros y emojis para hacer la experiencia más atractiva (🐾, ✅, 🎉).

    Opción especial "No coincide con estas opciones" en los niveles finales para permitir el aprendizaje.

2.3 Tecnologías y Herramientas Utilizadas

    Lenguaje de programación: Python 3

    Bibliotecas estándar:

        json: Para serializar y deserializar la estructura de datos.

        os: Para verificar la existencia del archivo de base de datos.

    Entorno de desarrollo: Visual Studio Code (VS Code)

    Control de versiones: Git y GitHub (para alojar y compartir el código)

3. CONCLUSIÓN

El proyecto "IA Adivinadora de Animales" ha logrado cumplir satisfactoriamente con todos los objetivos planteados inicialmente. Se ha desarrollado un sistema funcional que:

    Implementa un árbol de decisión complejo utilizando únicamente estructuras de datos nativas de Python (diccionarios anidados).

    Interactúa de manera efectiva con el usuario, guiándolo a través de preguntas lógicas hasta llegar a una conclusión.

    Incorpora un sistema de aprendizaje básico que permite ampliar la base de conocimientos del programa con cada partida.

    Garantiza la persistencia de los datos mediante el almacenamiento en archivos JSON, permitiendo que el conocimiento adquirido no se pierda entre ejecuciones.

Desde una perspectiva técnica, este proyecto demuestra competencias en áreas fundamentales de la programación como:

    Manejo de estructuras de datos complejas.

    Recorrido y manipulación de árboles.

    Entrada/salida de archivos.

    Manejo de excepciones.

    Interacción con el usuario a través de la consola.

Como líneas de trabajo futuro, se podrían considerar las siguientes mejoras:

    Implementar una interfaz gráfica para hacer el programa más accesible a usuarios no técnicos.

    Permitir la exportación del árbol de conocimiento a formatos como PDF o HTML para visualizarlo.

    Añadir la posibilidad de eliminar o modificar animales ya existentes en la base de datos.

    Incorporar un sistema de puntuación que evalúe la eficiencia del árbol (número de preguntas necesarias para adivinar).

En definitiva, el proyecto constituye una excelente base para entender conceptos fundamentales de inteligencia artificial y representación del conocimiento, con un resultado práctico, entretenido y funcional.
