🚀 Validador de Expresiones Regulares con Interfaz Gráfica 🖥️
¡Bienvenido al proyecto Validador de Expresiones Regulares! Esta aplicación te permite ingresar una expresión regular y validar múltiples cadenas de texto usando una interfaz gráfica amigable. Todo el proceso está respaldado por autómatas: primero se genera un NFA, luego se convierte en DFA, y finalmente se valida la cadena. Esta herramienta es ideal para estudiantes, profesores o cualquier persona que desee entender cómo funciona el proceso de validación de expresiones regulares de manera visual e interactiva.

📝 Características
Interfaz gráfica amigable creada con Tkinter.
Soporte para expresiones regulares básicas, incluyendo:
Concatenación (.): Ejemplo a.b.
Unión (|): Ejemplo a|b.
Cierre de Kleene (*): Ejemplo a*.
Conversión de expresión infija a notación postfija usando el algoritmo de Shunting Yard.
Generación de NFA y conversión a DFA para validar las cadenas.
Validación de múltiples cadenas con resultados instantáneos.
🛠️ Tecnologías Utilizadas
Python: Lenguaje principal del proyecto.
Tkinter: Para crear la interfaz gráfica de usuario.
Algoritmos de Autómatas:
NFA (Non-deterministic Finite Automaton).
DFA (Deterministic Finite Automaton).
Shunting Yard para la conversión de expresiones regulares.
⚙️ Instalación
Sigue estos pasos para ejecutar el proyecto en tu máquina local:

Clona este repositorio:

bash

git clone https://github.com/tu_usuario/validador-expresiones-regulares.git

Navega al directorio del proyecto:

bash

cd validador-expresiones-regulares

Instala las dependencias (Tkinter viene preinstalado con Python, pero asegúrate de tenerlo):

Asegúrate de tener Python 3 instalado.

Tkinter viene integrado con Python, por lo que no necesitas instalar nada adicional.

Ejecuta la aplicación:

bash

python validador_regex_tkinter.py
🚀 Cómo Usar la Aplicación
Ingresa una expresión regular en el campo de "Expresión Regular". Ejemplos:

a.b|c* para probar concatenación, unión, y cierre de Kleene.
a* para probar el cierre de Kleene sobre a.
Ingresa las cadenas a validar, cada una en una línea separada, en el área de "Cadenas a Validar".

Haz clic en el botón "Validar" para ver cuáles cadenas son aceptadas por la expresión regular ingresada.

📖 Ejemplos
Expresión Regular: ab*c
Cadenas Aceptadas: ac, abc, abbbc, etc.
Expresión Regular: (a|b)*c
Cadenas Aceptadas: c, ac, bc, aabbc, etc.
🤔 ¿Por qué este proyecto?
El propósito principal es proporcionar una herramienta educativa que haga más fácil la comprensión de cómo funcionan los autómatas y la validación de expresiones regulares. Es útil para estudiantes que están aprendiendo teoría de lenguajes formales y autómatas, así como para cualquier persona que quiera explorar cómo funcionan los motores de expresión regular bajo el capó.


🏗️ Estructura del Proyecto
regex_to_nfa.py: Contiene la lógica para convertir una expresión regular a un NFA.
nfa_to_dfa.py: Convierte el NFA en un DFA.
validador_regex_tkinter.py: Aplicación principal que maneja la interfaz gráfica y coordina los procesos de validación.
validate.py: Contiene la función para validar una cadena de texto utilizando el DFA generado.
error_handling.py: Gestión de errores y validación de la sintaxis de las expresiones regulares.
✨ Funcionalidades Futuras
Soporte para más operadores como +, ? y grupos ().
Guardado de resultados en un archivo para consultas posteriores.
Mejoras visuales en la interfaz gráfica.
🤝 Contribuir
Las contribuciones son siempre bienvenidas. Si tienes alguna idea para mejorar la aplicación, ¡no dudes en hacer un fork y enviar un pull request!

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz un commit (git commit -m 'Añadir nueva funcionalidad').
Haz un push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
📝 Licencia
Este proyecto está bajo la Licencia MIT. Puedes hacer lo que quieras con el código siempre y cuando des crédito a los autores originales.

📞 Contacto
Autor: Juan Esteban Astaiza Fuenmayor
Email: juan.astaizaf@uniquindio.edu.co
LinkedIn: www.linkedin.com/in/juanestebanastaizafuenmayor


