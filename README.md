# TurnAdventure

Un juego inspirado en Pokémon basado en combates por turnos completamente en línea de comandos.
<br>

<p align="center">
  ![Screenshot_20220427_143547](https://user-images.githubusercontent.com/84983282/165519872-a8c584ad-e0d4-4fa9-a4d4-594b72ba57e7.png)
</p>

<br>
Para jugar será recomendable tener el modulo de pygame instalado en python, se debería instalar automáticamente al ejecutar el archivo principal, en caso contrario usar 'pip install pygame' en la terminal.
<br>
<br>
Parámetros: music_off

# Known Issues

Failed loading libmpg123-0.dll: Se debe buscar y copiar el archivo 'libmpg123-0.dll' a C:\Windows\System32 y C:\Windows\SysWOW64

# Changelog

<h2>v0.15.1 Gardevoir</h2>

<b>Features</b>

- Se ha añadido la opción de salirse en el modo supervivencia.
- Se ha arreglado un fallo de compatibilidad para usuarios sin Pygame.
- Mejoras en la interfaz

<b>Bugs</b>

- Por encontrar.

<hr>

<h2>v0.15.0 Gardevoir</h2>

<b>Features</b>

- Se ha añadido una presentación al combate con los sonidos de cada personaje.

<b>Bugs</b>

- No se podrá entablar un combate sin la librería de Pygame.

<hr>

<h2>v0.14.3 Farfetch'd</h2>

<b>Features</b>

- Optimizaciones del código

<b>Bugs</b>

- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.14.2 Farfetch'd</h2>

<b>Features</b>

- Mejorada la gestión de errores en vista a poder usarse en Android.

<b>Bugs</b>

- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.14.1 Farfetch'd</h2>

<b>Features</b>

- Arreglado un bug el cual al perder demasiada vida en un turno no empezará el tema correspondiente.

<b>Bugs</b>

- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.14.0 Farfetch'd</h2>

<b>Features</b>

- Añadido un tema y animación de opening

<b>Bugs</b>

- Si se recibe demasiado daño en un solo turno no sonará el tema de low health.
- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.13.2 Espurr</h2>

<b>Features</b>

- Optimizaciones del código.
- Arreglado un error que no permitía ejecutar el juego sin la librería de Pygame.

<b>Bugs</b>

- Si se recibe demasiado daño en un solo turno no sonará el tema de low health.
- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.13.1 Espurr</h2>

<b>Features</b>

- Optimizaciones del código.

<b>Bugs</b>

- No se puede ejecutar el juego sin la librería de Pygame.
- Si se recibe demasiado daño en un solo turno no sonará el tema de low health.
- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.13.0 Espurr</h2>

<b>Features</b>

- Se ha arreglado un error que volvía a iniciar el tema de poca vida si volvías a recibir un golpe y sobrevives.
- Se ha corregido y mejorado la gestión de salud y su interfaz en batalla.

<b>Bugs</b>

- No se puede ejecutar el juego sin la librería de Pygame
- Si se recibe demasiado daño en un solo turno no sonará el tema de low health.
- Error al tener poca vida si no se tiene la librería de Pygame.

<hr>

<h2>v0.12.0 Dratini</h2>

<b>Features</b>

- Se ha mejorado la interfaz de batalla.
- Se ha añadido un tema al tener puntos de salud bajos.

<b>Bugs</b>

- Al tener pocos puntos de salud y sonar el tema correspondiente, volverá a iniciarse desde cero si se sobrevive a un golpe.
- No se puede ejecutar el juego sin la librería de Pygame

<hr>

<h2>v0.11.0 Chatot</h2>

<b>Features</b>

- Se ha añadido música y efectos nuevos.
- Ahora al golpear al adversario sonará un efecto dependiendo de si es normal o crítico.

<b>Bugs</b>

- No se puede ejecutar el juego sin la librería de Pygame

<hr>

<h2>v0.10.0 Beldum</h2>

<b>Features</b>

- Se ha añadido el parámetro music_off al iniciar mediante una terminal, para ello se empleará "Ruta_archivo/TurnAdventure/turnadventure.py music_off"
- Optimizaciones parciales y en curso del código.

<b>Bugs</b>

- Por encontrar.

<hr>

<h2>v0.9.0 Absol</h2>

<b>Features</b>

- Se ha mejorado el modo de combate random para recuperar el estado de tu personaje en la sesión y recuperar su vida en cada ronda.
- Mejoras en la interfaz.
- Optimizaciones parciales y en curso del código.

<b>Bugs</b>

- Por encontrar.

<hr>

<h2>v0.8.0</h2>

<b>Features</b>

- Mejoras en la interfaz de batalla.
- Se ha añadido una posibilidad de realizar ataque crítico.
- Arreglado el fallo anterior en la pantalla de selección.

<b>Bugs</b>

- Por encontrar.

<hr>

<h2>v0.7.0</h2>

<b>Features</b>

- Se ha añadido un modo supervivencia.
- Ahora se gestiona las dependencias y no pregunta cada vez que se inicia en distribuciones de linux (Debian, Arch).
- Cambios mayores en el sistema de combate.
- Equilibrios entre personajes.
- Añadido un apartado de visualización de estadísticas.

<b>Bugs</b>

- En la pantalla de selección de personaje si no se elige una opción planteada por defecto se usará siempre al perro.

<hr>

<h2>v0.6.0</h2>

<b>Features</b>

- Se ha añadido nueva música.
- Se ha añadido la posibilidad de elegir personaje en el modo random.
- Cambios menores en la interfaz de batalla.

<b>Bugs</b>

- En la pantalla de selección de personaje si no se elige una opción planteada por defecto se usará siempre al perro.

<hr>

<h2>v0.5.1</h2>

<b>Features</b>

- Se ha habilitado nuevamente la instalación de dependencias a través del CMD.

<b>Bugs</b>

- Ninguno encontrado.

<hr>

<h2>v0.5.0</h2>

<b>Features</b>

- Se ha añadido una función de compatibilidad en caso de no tener el módulo de pygame.

<b>Bugs</b>

- Ninguno encontrado.

<hr>

<h2>v0.4.0</h2>

<b>Features</b>

- Se ha cambiado la estructura de archivos.

<b>Bugs</b>

- Ninguno encontrado.

<hr>

<h2>v0.3.0</h2>

<b>Features</b>

- Arreglado un error al seleccionar el ataque "C" siempre realizaría el mismo daño independientemente del valor mostrado en pantalla.
- Se ha añadido un tema de victoria.

<b>Bugs</b>

- Ninguno encontrado.

<hr>

<h2>v0.2.3</h2>

<b>Features</b>

- Mejorada la compatibilidad con Windows.

<b>Bugs</b>

- El ataque C siempre realizará el mismo daño, independientemente del valor mostrado en pantalla.

<hr>

<h2>v0.2.2</h2>

<b>Features</b>

- Mejoras en la interfaz.

<b>Bugs</b>

- En windows se mostrarán errores y no permitirá jugar correctamente al seleccionar ataques.

<hr>
